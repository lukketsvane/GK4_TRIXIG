"use client";

import { create } from "zustand";
import { persist } from "zustand/middleware";
import {
  StructureType,
  SavedConfiguration,
  structurePresets,
  Evaluation,
} from "./structure-presets";

type SelectedComponent = "motor" | "battery" | null;

interface StructureState {
  currentType: StructureType | "custom";
  motorhusPosition: [number, number, number];
  motorhusRotation: [number, number, number];
  batteriPcbPosition: [number, number, number];
  batteriPcbRotation: [number, number, number];
  savedConfigurations: SavedConfiguration[];
  selectedComponent: SelectedComponent;
  showBoundingBoxes: boolean;
  showLabels: boolean;
  isIntersecting: boolean;
  cameraMode: "perspective" | "orthographic";
  showUI: boolean;
  viewLocked: boolean;

  setStructureType: (type: StructureType) => void;
  setMotorPosition: (position: [number, number, number]) => void;
  setMotorRotation: (rotation: [number, number, number]) => void;
  setBatteryPosition: (position: [number, number, number]) => void;
  setBatteryRotation: (rotation: [number, number, number]) => void;
  resetCurrentToPreset: () => void;
  resetMotorToPreset: () => void;
  resetBatteryToPreset: () => void;
  resetSelectedToPreset: () => void;
  saveConfiguration: (
    name: string,
    note?: string,
    evaluation?: Evaluation,
    thumbnail?: string
  ) => SavedConfiguration;
  updateConfiguration: (id: string, patch: Partial<SavedConfiguration>) => void;
  loadConfiguration: (id: string) => void;
  deleteConfiguration: (id: string) => void;
  quickSave: () => SavedConfiguration;
  setSelectedComponent: (component: SelectedComponent) => void;
  toggleBoundingBoxes: () => void;
  toggleLabels: () => void;
  setIntersecting: (b: boolean) => void;
  setCameraMode: (mode: "perspective" | "orthographic") => void;
  toggleUI: () => void;
  toggleViewLock: () => void;
  randomizeConfiguration: () => void;
}

export const useStructureStore = create<StructureState>()(
  persist(
    (set, get) => ({
      currentType: "inline",
      motorhusPosition: [0, 0, 0],
      motorhusRotation: [0, 0, 0],
      batteriPcbPosition: [-90, 0, 0],
      batteriPcbRotation: [0, 0, 0],
      savedConfigurations: [],
      selectedComponent: null,
      showBoundingBoxes: false,
      showLabels: true,
      isIntersecting: false,
      cameraMode: "orthographic",
      showUI: true,
      viewLocked: true,

      setStructureType: (type) => {
        const preset = structurePresets.find((p) => p.id === type);
        if (preset) {
          set({
            currentType: type,
            motorhusPosition: [...preset.motorhus.position],
            motorhusRotation: [...preset.motorhus.rotation],
            batteriPcbPosition: [...preset.batteri_pcb.position],
            batteriPcbRotation: [...preset.batteri_pcb.rotation],
            selectedComponent: null,
          });
        }
      },

      setMotorPosition: (position) =>
        set({ motorhusPosition: position, currentType: "custom" }),
      setMotorRotation: (rotation) =>
        set({ motorhusRotation: rotation, currentType: "custom" }),
      setBatteryPosition: (position) =>
        set({ batteriPcbPosition: position, currentType: "custom" }),
      setBatteryRotation: (rotation) =>
        set({ batteriPcbRotation: rotation, currentType: "custom" }),

      resetCurrentToPreset: () => {
        const t = get().currentType;
        if (t === "custom") return;
        const preset = structurePresets.find((p) => p.id === t);
        if (!preset) return;
        set({
          motorhusPosition: [...preset.motorhus.position],
          motorhusRotation: [...preset.motorhus.rotation],
          batteriPcbPosition: [...preset.batteri_pcb.position],
          batteriPcbRotation: [...preset.batteri_pcb.rotation],
        });
      },

      resetMotorToPreset: () => {
        const t = get().currentType;
        const preset =
          t === "custom" ? null : structurePresets.find((p) => p.id === t);
        const target = preset
          ? preset.motorhus
          : { position: [0, 0, 0], rotation: [0, 0, 0] };
        set({
          motorhusPosition: [...(target.position as [number, number, number])],
          motorhusRotation: [...(target.rotation as [number, number, number])],
        });
      },

      resetBatteryToPreset: () => {
        const t = get().currentType;
        const preset =
          t === "custom" ? null : structurePresets.find((p) => p.id === t);
        const target = preset
          ? preset.batteri_pcb
          : { position: [-90, 0, 0], rotation: [0, 0, 0] };
        set({
          batteriPcbPosition: [
            ...(target.position as [number, number, number]),
          ],
          batteriPcbRotation: [
            ...(target.rotation as [number, number, number]),
          ],
        });
      },

      resetSelectedToPreset: () => {
        const sel = get().selectedComponent;
        if (sel === "motor") get().resetMotorToPreset();
        else if (sel === "battery") get().resetBatteryToPreset();
      },

      saveConfiguration: (name, note, evaluation, thumbnail) => {
        const state = get();
        const newConfig: SavedConfiguration = {
          id: `config-${Date.now()}`,
          name,
          type: state.currentType,
          motorhus: {
            position: [...state.motorhusPosition],
            rotation: [...state.motorhusRotation],
          },
          batteri_pcb: {
            position: [...state.batteriPcbPosition],
            rotation: [...state.batteriPcbRotation],
          },
          note,
          evaluation,
          thumbnail,
          saved: new Date().toISOString().split("T")[0],
        };
        set({
          savedConfigurations: [...state.savedConfigurations, newConfig],
        });
        return newConfig;
      },

      updateConfiguration: (id, patch) => {
        set({
          savedConfigurations: get().savedConfigurations.map((c) =>
            c.id === id ? { ...c, ...patch } : c
          ),
        });
      },

      loadConfiguration: (id) => {
        const config = get().savedConfigurations.find((c) => c.id === id);
        if (config) {
          set({
            currentType: config.type,
            motorhusPosition: [...config.motorhus.position],
            motorhusRotation: [...config.motorhus.rotation],
            batteriPcbPosition: [...config.batteri_pcb.position],
            batteriPcbRotation: [...config.batteri_pcb.rotation],
            selectedComponent: null,
          });
        }
      },

      deleteConfiguration: (id) => {
        set({
          savedConfigurations: get().savedConfigurations.filter(
            (c) => c.id !== id
          ),
        });
      },

      quickSave: () => {
        const state = get();
        const id = `config-${Date.now()}`;
        const name = `Variant ${state.savedConfigurations.length + 1}`;
        const thumbnail = captureCanvasPng() ?? undefined;
        
        const newConfig: SavedConfiguration = {
          id,
          name,
          type: state.currentType,
          motorhus: {
            position: [...state.motorhusPosition],
            rotation: [...state.motorhusRotation],
          },
          batteri_pcb: {
            position: [...state.batteriPcbPosition],
            rotation: [...state.batteriPcbRotation],
          },
          saved: new Date().toISOString().split("T")[0],
          thumbnail,
        };

        set({
          savedConfigurations: [...state.savedConfigurations, newConfig],
        });
        return newConfig;
      },

      setSelectedComponent: (component) =>
        set({ selectedComponent: component }),
      toggleBoundingBoxes: () =>
        set({ showBoundingBoxes: !get().showBoundingBoxes }),
      toggleLabels: () => set({ showLabels: !get().showLabels }),
      setIntersecting: (b) => {
        if (get().isIntersecting !== b) set({ isIntersecting: b });
      },
      setCameraMode: (mode) => set({ cameraMode: mode }),
      toggleUI: () => set({ showUI: !get().showUI }),
      toggleViewLock: () => set({ viewLocked: !get().viewLocked }),

      randomizeConfiguration: () => {
        const getRandomCleanRot = () => [0, 90, 180, 270, -90][Math.floor(Math.random() * 5)];
        
        const dist = 400; 
        
        const mPos: [number, number, number] = [
          Math.round((Math.random() - 0.5) * 80),
          Math.round((Math.random() - 0.5) * 80),
          Math.round((Math.random() - 0.5) * 80),
        ];
        const mRot: [number, number, number] = [getRandomCleanRot(), getRandomCleanRot(), getRandomCleanRot()];
        
        const directions = [[1,0,0], [-1,0,0], [0,1,0], [0,-1,0], [0,0,1], [0,0,-1]];
        const dir = directions[Math.floor(Math.random() * directions.length)];
        
        const bPos: [number, number, number] = [
          Math.round(mPos[0] + dir[0] * dist),
          Math.round(mPos[1] + dir[1] * dist),
          Math.round(mPos[2] + dir[2] * dist),
        ];
        
        if (dir[0] === 0) bPos[0] += Math.round((Math.random() - 0.5) * 120);
        if (dir[1] === 0) bPos[1] += Math.round((Math.random() - 0.5) * 120);
        if (dir[2] === 0) bPos[2] += Math.round((Math.random() - 0.5) * 120);

        const bRot: [number, number, number] = [getRandomCleanRot(), getRandomCleanRot(), getRandomCleanRot()];

        set({
          motorhusPosition: mPos,
          motorhusRotation: mRot,
          batteriPcbPosition: bPos,
          batteriPcbRotation: bRot,
          currentType: "custom",
          selectedComponent: null
        });
      },
    }),
    {
      name: "trixig-structure-storage",
      partialize: (state) => ({
        savedConfigurations: state.savedConfigurations,
      }),
    }
  )
);

// ---- Eksport-hjelparar ----

export function buildExportJson(opts?: { name?: string; note?: string }) {
  const s = useStructureStore.getState();
  return {
    name: opts?.name ?? `struktur_${s.currentType}`,
    type: s.currentType,
    motorhus: {
      position: s.motorhusPosition,
      rotation: s.motorhusRotation,
    },
    batteri_pcb: {
      position: s.batteriPcbPosition,
      rotation: s.batteriPcbRotation,
    },
    note: opts?.note ?? "",
    saved: new Date().toISOString().split("T")[0],
  };
}

export function downloadBlob(filename: string, blob: Blob) {
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

export function captureCanvasPng(): string | null {
  const canvas =
    document.querySelector<HTMLCanvasElement>("canvas[data-engine]") ??
    document.querySelector<HTMLCanvasElement>("canvas");
  if (!canvas) return null;
  try {
    return canvas.toDataURL("image/png");
  } catch {
    return null;
  }
}
