"use client";

import * as THREE from "three";
import { useRef, Suspense, useMemo, useState, useLayoutEffect, useEffect } from "react";
import { Canvas, useFrame, useThree } from "@react-three/fiber";
import {
  OrbitControls,
  Environment,
  useGLTF,
  PivotControls,
  GizmoHelper,
  GizmoViewcube,
} from "@react-three/drei";
import { useStructureStore } from "@/lib/structure-store";
import { Button } from "@/components/ui/button";
import { Eye, EyeOff, Square, RefreshCw, PanelLeftClose, PanelLeftOpen, Save, Lock, LockOpen } from "lucide-react";

const MOTOR_URL = "/motorhus.glb";
const BATTERY_URL = "/batteri_pcb.glb";
const SCALE_FACTOR = 0.02;
const POSITION_SCALE = 0.001;

function ComponentModel({
  type,
  url,
  color,
}: {
  type: "motor" | "battery";
  url: string;
  color: string;
}) {
  const { scene } = useGLTF(url);
  
  const position = useStructureStore((s) =>
    type === "motor" ? s.motorhusPosition : s.batteriPcbPosition
  );
  const rotation = useStructureStore((s) =>
    type === "motor" ? s.motorhusRotation : s.batteriPcbRotation
  );
  const selectedComponent = useStructureStore((s) => s.selectedComponent);
  const showBoundingBoxes = useStructureStore((s) => s.showBoundingBoxes);
  const isIntersecting = useStructureStore((s) => s.isIntersecting);
  const setSelectedComponent = useStructureStore((s) => s.setSelectedComponent);
  const setMotorPosition = useStructureStore((s) => s.setMotorPosition);
  const setMotorRotation = useStructureStore((s) => s.setMotorRotation);
  const setBatteryPosition = useStructureStore((s) => s.setBatteryPosition);
  const setBatteryRotation = useStructureStore((s) => s.setBatteryRotation);

  const isSelected = selectedComponent === type;

  // Sync material
  useMemo(() => {
    scene.traverse((child) => {
      if ((child as THREE.Mesh).isMesh) {
        const m = child as THREE.Mesh;
        m.material = new THREE.MeshStandardMaterial({
          color,
          metalness: 0.15,
          roughness: 0.4,
        });
      }
    });
  }, [scene, color]);

  const bbox = useMemo(() => {
    const b = new THREE.Box3().setFromObject(scene);
    const size = new THREE.Vector3();
    const center = new THREE.Vector3();
    if (!b.isEmpty()) {
      b.getSize(size);
      b.getCenter(center);
    } else {
      size.set(1, 1, 1);
      center.set(0, 0, 0);
    }
    return { size, center };
  }, [scene]);

  // Create matrix for PivotControls
  const matrix = useMemo(() => {
    const m = new THREE.Matrix4();
    const euler = new THREE.Euler(
      (rotation[0] * Math.PI) / 180,
      (rotation[1] * Math.PI) / 180,
      (rotation[2] * Math.PI) / 180
    );
    const quaternion = new THREE.Quaternion().setFromEuler(euler);
    m.compose(
      new THREE.Vector3(
        position[0] * POSITION_SCALE,
        position[1] * POSITION_SCALE,
        position[2] * POSITION_SCALE
      ),
      quaternion,
      new THREE.Vector3(1, 1, 1)
    );
    return m;
  }, [position, rotation]);

  const handleDrag = (m: THREE.Matrix4) => {
    const pos = new THREE.Vector3();
    const quat = new THREE.Quaternion();
    const scale = new THREE.Vector3();
    m.decompose(pos, quat, scale);

    const euler = new THREE.Euler().setFromQuaternion(quat);
    
    const newPos: [number, number, number] = [
      Math.round(pos.x / POSITION_SCALE),
      Math.round(pos.y / POSITION_SCALE),
      Math.round(pos.z / POSITION_SCALE),
    ];
    const newRot: [number, number, number] = [
      Math.round((euler.x * 180) / Math.PI),
      Math.round((euler.y * 180) / Math.PI),
      Math.round((euler.z * 180) / Math.PI),
    ];

    if (type === "motor") {
      setMotorPosition(newPos);
      setMotorRotation(newRot);
    } else {
      setBatteryPosition(newPos);
      setBatteryRotation(newRot);
    }
  };

  return (
    <PivotControls
      enabled={isSelected}
      matrix={matrix}
      anchor={[0, 0, 0]}
      depthTest={false}
      lineWidth={2}
      fixed={true}
      scale={75}
      activeAxes={[true, true, true]}
      snap={{ rotation: Math.PI / 36 }}
      disableSliders
      annotations={false}
      onDrag={handleDrag}
    >
      <group
        onClick={(e) => {
          e.stopPropagation();
          setSelectedComponent(isSelected ? null : type);
        }}
        onPointerOver={() => (document.body.style.cursor = "pointer")}
        onPointerOut={() => (document.body.style.cursor = "auto")}
      >
        <primitive object={scene} scale={SCALE_FACTOR} />

        {(showBoundingBoxes || (isIntersecting && isSelected)) && (
          <lineSegments
            position={[
              bbox.center.x * SCALE_FACTOR,
              bbox.center.y * SCALE_FACTOR,
              bbox.center.z * SCALE_FACTOR,
            ]}
          >
            <edgesGeometry
              args={[
                new THREE.BoxGeometry(
                  Math.max(0.001, bbox.size.x * SCALE_FACTOR),
                  Math.max(0.001, bbox.size.y * SCALE_FACTOR),
                  Math.max(0.001, bbox.size.z * SCALE_FACTOR)
                ),
              ]}
            />
            <lineBasicMaterial 
              color={isIntersecting ? "#ff0000" : color} 
              transparent 
              opacity={0.8} 
              linewidth={isIntersecting ? 2 : 1}
            />
          </lineSegments>
        )}
      </group>
    </PivotControls>
  );
}

function CollisionDetector() {
  const motorPos = useStructureStore((s) => s.motorhusPosition);
  const motorRot = useStructureStore((s) => s.motorhusRotation);
  const batteryPos = useStructureStore((s) => s.batteriPcbPosition);
  const batteryRot = useStructureStore((s) => s.batteriPcbRotation);
  const setIntersecting = useStructureStore((s) => s.setIntersecting);

  const { scene: motorScene } = useGLTF(MOTOR_URL);
  const { scene: batteryScene } = useGLTF(BATTERY_URL);

  const motorBox = useMemo(() => new THREE.Box3(), []);
  const batteryBox = useMemo(() => new THREE.Box3(), []);
  const motorMatrix = useMemo(() => new THREE.Matrix4(), []);
  const batteryMatrix = useMemo(() => new THREE.Matrix4(), []);

  const motorBaseBox = useMemo(() => {
    const b = new THREE.Box3().setFromObject(motorScene);
    b.min.multiplyScalar(SCALE_FACTOR);
    b.max.multiplyScalar(SCALE_FACTOR);
    return b;
  }, [motorScene]);

  const batteryBaseBox = useMemo(() => {
    const b = new THREE.Box3().setFromObject(batteryScene);
    b.min.multiplyScalar(SCALE_FACTOR);
    b.max.multiplyScalar(SCALE_FACTOR);
    return b;
  }, [batteryScene]);

  useFrame(() => {
    motorMatrix.makeRotationFromEuler(new THREE.Euler(
      (motorRot[0] * Math.PI) / 180,
      (motorRot[1] * Math.PI) / 180,
      (motorRot[2] * Math.PI) / 180
    ));
    motorMatrix.setPosition(
      motorPos[0] * POSITION_SCALE,
      motorPos[1] * POSITION_SCALE,
      motorPos[2] * POSITION_SCALE
    );

    batteryMatrix.makeRotationFromEuler(new THREE.Euler(
      (batteryRot[0] * Math.PI) / 180,
      (batteryRot[1] * Math.PI) / 180,
      (batteryRot[2] * Math.PI) / 180
    ));
    batteryMatrix.setPosition(
      batteryPos[0] * POSITION_SCALE,
      batteryPos[1] * POSITION_SCALE,
      batteryPos[2] * POSITION_SCALE
    );

    motorBox.copy(motorBaseBox).applyMatrix4(motorMatrix);
    batteryBox.copy(batteryBaseBox).applyMatrix4(batteryMatrix);

    setIntersecting(motorBox.intersectsBox(batteryBox));
  });

  return null;
}

function KeyboardControls() {
  const setSelectedComponent = useStructureStore((s) => s.setSelectedComponent);
  const resetSelected = useStructureStore((s) => s.resetSelectedToPreset);
  const randomizeConfiguration = useStructureStore((s) => s.randomizeConfiguration);
  const toggleUI = useStructureStore((s) => s.toggleUI);
  const quickSave = useStructureStore((s) => s.quickSave);
  const toggleViewLock = useStructureStore((s) => s.toggleViewLock);
  const { camera, controls } = useThree();

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.target instanceof HTMLInputElement || e.target instanceof HTMLTextAreaElement) return;

      if (e.key === "Escape") setSelectedComponent(null);
      if (e.key === "r" || e.key === "R") resetSelected();
      if (e.key === "q" || e.key === "Q") randomizeConfiguration();
      if (e.key === "h" || e.key === "H") toggleUI();
      if (e.key === "s" || e.key === "S") quickSave();
      if (e.key === "l" || e.key === "L") toggleViewLock();

      if (e.key === "1") {
        camera.position.set(4, 0, 0); // Left View
        (controls as any)?.target.set(0, 0, 0);
      }
      if (e.key === "2") {
        camera.position.set(0, 0, 4); // Front
        (controls as any)?.target.set(0, 0, 0);
      }
      if (e.key === "3") {
        camera.position.set(0, 4, 0); // Top
        (controls as any)?.target.set(0, 0, 0);
      }
      if (e.key === "4") {
        camera.position.set(2.5, 1.8, 3); // Perspective
        (controls as any)?.target.set(0, 0, 0);
      }

      if (e.key === "Delete" || e.key === "Backspace") {
        setSelectedComponent(null);
      }
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [setSelectedComponent, resetSelected, randomizeConfiguration, toggleUI, quickSave, toggleViewLock, camera, controls]);

  return null;
}

function Scene() {
  const viewLocked = useStructureStore((s) => s.viewLocked);

  return (
    <>
      <color attach="background" args={["#ffffff"]} />
      <ambientLight intensity={0.8} />
      <pointLight position={[10, 10, 10]} intensity={1.5} />
      <pointLight position={[-10, 5, -10]} intensity={0.5} />

      <Suspense fallback={null}>
        <ComponentModel
          type="motor"
          url={MOTOR_URL}
          color="#003F94"
        />
        <ComponentModel
          type="battery"
          url={BATTERY_URL}
          color="#FFD600"
        />
        <CollisionDetector />
      </Suspense>

      <KeyboardControls />

      <GizmoHelper alignment="bottom-right" margin={[100, 100]}>
        <GizmoViewcube />
      </GizmoHelper>

      <Suspense fallback={null}>
        <Environment preset="city" />
      </Suspense>

      <OrbitControls
        enablePan={!viewLocked}
        enableZoom={!viewLocked}
        enableRotate={!viewLocked}
        minDistance={0.1}
        maxDistance={50}
        makeDefault
      />

      <mesh
        visible={false}
        position={[0, 0, 0]}
        onClick={() => useStructureStore.getState().setSelectedComponent(null)}
      >
        <planeGeometry args={[100, 100]} />
      </mesh>
    </>
  );
}

export function Scene3D() {
  const cameraMode = useStructureStore((s) => s.cameraMode);
  const setCameraMode = useStructureStore((s) => s.setCameraMode);
  const randomize = useStructureStore((s) => s.randomizeConfiguration);
  const showLabels = useStructureStore((s) => s.showLabels);
  const toggleLabels = useStructureStore((s) => s.toggleLabels);
  const showBoundingBoxes = useStructureStore((s) => s.showBoundingBoxes);
  const toggleBoundingBoxes = useStructureStore((s) => s.toggleBoundingBoxes);
  const showUI = useStructureStore((s) => s.showUI);
  const toggleUI = useStructureStore((s) => s.toggleUI);
  const quickSave = useStructureStore((s) => s.quickSave);
  const viewLocked = useStructureStore((s) => s.viewLocked);
  const toggleViewLock = useStructureStore((s) => s.toggleViewLock);

  return (
    <div className="relative h-full w-full touch-none">
      <Canvas
        camera={{ position: [4, 0, 0], fov: 45, zoom: 40 }}
        orthographic={cameraMode === "orthographic"}
        gl={{ preserveDrawingBuffer: true, antialias: true }}
        onPointerMissed={() =>
          useStructureStore.getState().setSelectedComponent(null)
        }
      >
        <Scene />
      </Canvas>

      <div className="pointer-events-none absolute inset-x-0 top-0 flex items-start justify-end p-2 sm:p-3">
        <div className="pointer-events-auto flex items-center gap-1.5">
          <Button
            onClick={toggleViewLock}
            variant={viewLocked ? "default" : "outline"}
            size="icon"
            className={`h-9 w-9 backdrop-blur-sm ${viewLocked ? "" : "bg-card/80"}`}
            title="Lås visning (L)"
          >
            {viewLocked ? <Lock className="h-4 w-4" /> : <LockOpen className="h-4 w-4" />}
          </Button>

          <Button
            onClick={quickSave}
            variant="outline"
            size="icon"
            className="h-9 w-9 bg-card/80 backdrop-blur-sm"
            title="Hurtiglagre (S)"
          >
            <Save className="h-4 w-4" />
          </Button>

          <Button
            onClick={toggleUI}
            variant="outline"
            size="icon"
            className="h-9 w-9 bg-card/80 backdrop-blur-sm hidden md:flex"
            title="Skjul grensesnitt (H)"
          >
            {showUI ? <PanelLeftClose className="h-4 w-4" /> : <PanelLeftOpen className="h-4 w-4" />}
          </Button>

          <Button
            onClick={randomize}
            variant="outline"
            size="icon"
            className="h-9 w-9 bg-card/80 backdrop-blur-sm"
            title="Tilfeldig (Q)"
          >
            <RefreshCw className="h-4 w-4" />
          </Button>
          
          <Button
            onClick={() => setCameraMode(cameraMode === "perspective" ? "orthographic" : "perspective")}
            variant="outline"
            size="icon"
            className="h-9 w-9 bg-card/80 backdrop-blur-sm"
            title={cameraMode === "perspective" ? "Bytt til ortografisk" : "Bytt til perspektiv"}
          >
            <div className="font-mono text-[10px] font-bold">
              {cameraMode === "perspective" ? "P" : "O"}
            </div>
          </Button>

          <Button
            onClick={toggleLabels}
            variant="outline"
            size="icon"
            className="h-9 w-9 bg-card/80 backdrop-blur-sm"
            title="Namn"
          >
            {showLabels ? <Eye className="h-4 w-4" /> : <EyeOff className="h-4 w-4" />}
          </Button>

          <Button
            onClick={toggleBoundingBoxes}
            variant="outline"
            size="icon"
            className={`h-9 w-9 backdrop-blur-sm ${
              showBoundingBoxes ? "bg-foreground text-background" : "bg-card/80"
            }`}
            title="Bounding box"
          >
            <Square className="h-4 w-4" />
          </Button>
        </div>
      </div>
    </div>
  );
}

useGLTF.preload(MOTOR_URL);
useGLTF.preload(BATTERY_URL);
