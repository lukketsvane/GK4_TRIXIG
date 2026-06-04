"use client";

import dynamic from "next/dynamic";
import { useMemo, useState, useEffect } from "react";
import {
  useStructureStore,
  buildExportJson,
  captureCanvasPng,
  downloadBlob,
} from "@/lib/structure-store";
import {
  evaluationKeys,
  evaluationLabels,
  Evaluation,
} from "@/lib/structure-presets";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Slider } from "@/components/ui/slider";
import { Separator } from "@/components/ui/separator";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogFooter,
} from "@/components/ui/dialog";
import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet";
import {
  Save,
  Trash2,
  Menu,
  FolderOpen,
  Download,
  Image as ImageIcon,
  RefreshCw,
  X,
} from "lucide-react";

const Scene3D = dynamic(
  () => import("@/components/scene-3d").then((mod) => mod.Scene3D),
  {
    ssr: false,
    loading: () => (
      <div className="flex h-full w-full items-center justify-center bg-white">
        <div className="h-6 w-6 animate-spin rounded-full border-2 border-primary border-t-transparent" />
      </div>
    ),
  }
);

/* ---------- Building blocks ---------- */

function AxisInput({
  label,
  value,
  min,
  max,
  step,
  onChange,
}: {
  label: string;
  value: number;
  min: number;
  max: number;
  step: number;
  onChange: (v: number) => void;
}) {
  const [localValue, setLocalValue] = useState(value.toString());

  useEffect(() => {
    setLocalValue(value.toString());
  }, [value]);

  const handleBlur = () => {
    let n = parseFloat(localValue);
    if (isNaN(n)) n = value;
    n = Math.max(min, Math.min(max, n));
    onChange(n);
    setLocalValue(n.toString());
  };

  return (
    <div className="flex items-center gap-2">
      <span className="w-4 font-mono text-[10px] text-muted-foreground uppercase">
        {label}
      </span>
      <Slider
        value={[value]}
        min={min}
        max={max}
        step={step}
        onValueChange={(v) => onChange(v[0] ?? 0)}
        className="flex-1"
      />
      <Input
        value={localValue}
        onChange={(e) => setLocalValue(e.target.value)}
        onBlur={handleBlur}
        onKeyDown={(e) => {
          if (e.key === "Enter") handleBlur();
        }}
        className="h-6 w-14 border-none bg-transparent px-1 text-right font-mono text-[10px] tabular-nums focus-visible:ring-0 focus-visible:ring-offset-0"
      />
    </div>
  );
}

function ComponentTransformBody({
  which,
  compact = false,
}: {
  which: "motor" | "battery";
  compact?: boolean;
}) {
  const pos = useStructureStore((s) =>
    which === "motor" ? s.motorhusPosition : s.batteriPcbPosition
  );
  const rot = useStructureStore((s) =>
    which === "motor" ? s.motorhusRotation : s.batteriPcbRotation
  );
  const setPos = useStructureStore((s) =>
    which === "motor" ? s.setMotorPosition : s.setBatteryPosition
  );
  const setRot = useStructureStore((s) =>
    which === "motor" ? s.setMotorRotation : s.setBatteryRotation
  );

  const setAxis =
    (
      arr: [number, number, number],
      setter: (v: [number, number, number]) => void,
      idx: number
    ) =>
    (v: number) => {
      const next: [number, number, number] = [arr[0], arr[1], arr[2]];
      next[idx] = v;
      setter(next);
    };

  return (
    <div className={compact ? "space-y-1" : "space-y-1.5"}>
      <div className="text-[9px] uppercase tracking-wider text-muted-foreground/60 mb-0.5">Posisjon (mm)</div>
      <AxisInput label="x" value={pos[0]} min={-200} max={200} step={1} onChange={setAxis(pos, setPos, 0)} />
      <AxisInput label="y" value={pos[1]} min={-200} max={200} step={1} onChange={setAxis(pos, setPos, 1)} />
      <AxisInput label="z" value={pos[2]} min={-200} max={200} step={1} onChange={setAxis(pos, setPos, 2)} />
      <div className="my-1.5 h-px bg-border/40" />
      <div className="text-[9px] uppercase tracking-wider text-muted-foreground/60 mb-0.5">Rotasjon (gradar)</div>
      <AxisInput label="x" value={rot[0]} min={-180} max={180} step={1} onChange={setAxis(rot, setRot, 0)} />
      <AxisInput label="y" value={rot[1]} min={-180} max={180} step={1} onChange={setAxis(rot, setRot, 1)} />
      <AxisInput label="z" value={rot[2]} min={-180} max={180} step={1} onChange={setAxis(rot, setRot, 2)} />
    </div>
  );
}

function ComponentTransformPanel({
  which,
}: {
  which: "motor" | "battery";
}) {
  const setSelected = useStructureStore((s) => s.setSelectedComponent);
  const selected = useStructureStore((s) => s.selectedComponent);
  const resetSelected = useStructureStore((s) => 
    which === "motor" ? s.resetMotorToPreset : s.resetBatteryToPreset
  );
  const isSelected = selected === which;
  const isIntersecting = useStructureStore((s) => s.isIntersecting);
  const color = which === "motor" ? "#003F94" : "#FFD600";
  const name = which === "motor" ? "motorhus" : "batteri_pcb";

  return (
    <div
      className={`rounded-md border p-2.5 transition-all ${
        isSelected ? "border-foreground/40 bg-muted/40 shadow-sm" : "border-border"
      } ${isIntersecting && isSelected ? "ring-1 ring-destructive/30" : ""}`}
    >
      <div className="mb-2 flex w-full items-center justify-between">
        <button
          onClick={() => setSelected(isSelected ? null : which)}
          className="flex items-center gap-2"
        >
          <span
            className="inline-block h-2.5 w-2.5 rounded-sm"
            style={{ backgroundColor: color }}
          />
          <span className="font-mono text-[11px]">{name}</span>
        </button>
        {isSelected && (
          <button
            onClick={resetSelected}
            className="text-muted-foreground hover:text-foreground p-1"
            title="Tilbakestill (R)"
          >
            <RefreshCw className="h-3 w-3" />
          </button>
        )}
      </div>
      <ComponentTransformBody which={which} />
    </div>
  );
}

function EvaluationStars({
  value,
  onChange,
}: {
  value: number;
  onChange: (v: number) => void;
}) {
  return (
    <div className="flex items-center gap-0.5">
      {[1, 2, 3].map((n) => (
        <button
          key={n}
          onClick={() => onChange(value === n ? 0 : n)}
          className={`h-3.5 w-3.5 rounded-full transition-colors ${
            n <= value
              ? "bg-foreground"
              : "border border-border bg-transparent hover:bg-muted"
          }`}
          aria-label={`Sett ${n}`}
        />
      ))}
    </div>
  );
}

function SaveDialog({
  open,
  onOpenChange,
}: {
  open: boolean;
  onOpenChange: (b: boolean) => void;
}) {
  const [name, setName] = useState("");
  const [note, setNote] = useState("");
  const [evaluation, setEvaluation] = useState<Evaluation>({});
  const save = useStructureStore((s) => s.saveConfiguration);
  const currentType = useStructureStore((s) => s.currentType);

  const handleSave = () => {
    const finalName =
      name.trim() ||
      `struktur_${currentType}_${new Date()
        .toISOString()
        .replace(/[-:T]/g, "")
        .slice(0, 12)}`;
    const thumb = captureCanvasPng() ?? undefined;
    save(finalName, note.trim() || undefined, evaluation, thumb);
    setName("");
    setNote("");
    setEvaluation({});
    onOpenChange(false);
  };

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="max-w-md">
        <DialogHeader>
          <DialogTitle>Lagra variant</DialogTitle>
        </DialogHeader>
        <div className="space-y-3 pt-2">
          <Input
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder={`struktur_${currentType}`}
            onKeyDown={(e) => {
              if (e.key === "Enter" && !e.shiftKey) handleSave();
            }}
          />
          <Textarea
            value={note}
            onChange={(e) => setNote(e.target.value)}
            placeholder="Notat ..."
            rows={2}
          />
          <Separator />
          <div className="space-y-1.5">
            {evaluationKeys.map((k) => (
              <div
                key={k}
                className="flex items-center justify-between text-xs"
              >
                <span>{evaluationLabels[k]}</span>
                <EvaluationStars
                  value={evaluation[k] ?? 0}
                  onChange={(v) =>
                    setEvaluation((prev) => ({ ...prev, [k]: v }))
                  }
                />
              </div>
            ))}
          </div>
        </div>
        <DialogFooter>
          <Button variant="outline" onClick={() => onOpenChange(false)}>
            Avbryt
          </Button>
          <Button onClick={handleSave}>Lagra</Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}

function SavedConfigCard({ id }: { id: string }) {
  const config = useStructureStore((s) =>
    s.savedConfigurations.find((c) => c.id === id)
  );
  const load = useStructureStore((s) => s.loadConfiguration);
  const del = useStructureStore((s) => s.deleteConfiguration);

  if (!config) return null;

  const exportJson = () => {
    const blob = new Blob([JSON.stringify(config, null, 2)], {
      type: "application/json",
    });
    downloadBlob(`${config.name}.json`, blob);
  };

  return (
    <div className="group overflow-hidden rounded-md border bg-card">
      <button
        className="block w-full text-left"
        onClick={() => load(config.id)}
        title="Last"
      >
        {config.thumbnail ? (
          // eslint-disable-next-line @next/next/no-img-element
          <img
            src={config.thumbnail}
            alt={config.name}
            className="aspect-video w-full bg-muted object-cover"
          />
        ) : (
          <div className="flex aspect-video w-full items-center justify-center bg-muted/50 text-[10px] text-muted-foreground">
            —
          </div>
        )}
      </button>
      <div className="p-2">
        <div className="flex items-start justify-between gap-1">
          <div className="min-w-0 flex-1">
            <div className="truncate text-[11px] font-medium">
              {config.name}
            </div>
            <div className="font-mono text-[9px] text-muted-foreground">
              {config.type} · {config.saved}
            </div>
          </div>
          <div className="flex shrink-0 gap-0.5">
            <button
              onClick={exportJson}
              className="rounded p-1 text-muted-foreground hover:bg-muted"
              title="JSON"
            >
              <Download className="h-3 w-3" />
            </button>
            <button
              onClick={() => del(config.id)}
              className="rounded p-1 text-muted-foreground hover:bg-destructive/10 hover:text-destructive"
              title="Slett"
            >
              <Trash2 className="h-3 w-3" />
            </button>
          </div>
        </div>
        {config.note && (
          <div className="mt-1 line-clamp-2 text-[10px] text-muted-foreground">
            {config.note}
          </div>
        )}
        {config.evaluation && Object.keys(config.evaluation).length > 0 && (
          <div className="mt-1.5 flex flex-wrap gap-1">
            {evaluationKeys.map((k) => {
              const v = config.evaluation?.[k] ?? 0;
              if (!v) return null;
              return (
                <span
                  key={k}
                  className="rounded bg-muted px-1 py-0.5 font-mono text-[8px]"
                  title={evaluationLabels[k]}
                >
                  {k.slice(0, 3)}·{v}
                </span>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
}

function SavedList() {
  const savedConfigurations = useStructureStore((s) => s.savedConfigurations);

  if (savedConfigurations.length === 0) {
    return (
      <div className="py-10 text-center text-[10px] text-muted-foreground">
        Ingen lagra.
      </div>
    );
  }

  return (
    <div className="space-y-1.5">
      {savedConfigurations
        .slice()
        .reverse()
        .map((c) => (
          <SavedConfigCard key={c.id} id={c.id} />
        ))}
    </div>
  );
}

function MobileTransformSheet() {
  const selected = useStructureStore((s) => s.selectedComponent);
  const setSelected = useStructureStore((s) => s.setSelectedComponent);

  const open = selected !== null;
  const color = selected === "motor" ? "#003F94" : "#FFD600";
  const name = selected === "motor" ? "motorhus" : "batteri_pcb";

  return (
    <div
      className={`pointer-events-none absolute inset-x-0 bottom-0 z-30 transition-transform duration-200 md:hidden ${
        open ? "translate-y-0" : "translate-y-full"
      }`}
      style={{ paddingBottom: "env(safe-area-inset-bottom)" }}
    >
      <div className="pointer-events-auto mx-2 mb-2 rounded-2xl border bg-card/95 p-3 shadow-xl backdrop-blur">
        <div className="mb-2 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <span
              className="inline-block h-3 w-3 rounded-sm"
              style={{ backgroundColor: color }}
            />
            <span className="font-mono text-xs">{name}</span>
          </div>
          <button
            onClick={() => setSelected(null)}
            className="rounded p-1 text-muted-foreground hover:bg-muted"
            title="Lukk"
          >
            <X className="h-4 w-4" />
          </button>
        </div>
        {selected && <ComponentTransformBody which={selected} compact />}
      </div>
    </div>
  );
}

export default function HomePage() {
  const [saveOpen, setSaveOpen] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false);

  const currentType = useStructureStore((s) => s.currentType);
  const savedConfigurations = useStructureStore((s) => s.savedConfigurations);
  const showUI = useStructureStore((s) => s.showUI);
  const cameraMode = useStructureStore((s) => s.cameraMode);
  const setCameraMode = useStructureStore((s) => s.setCameraMode);
  const randomize = useStructureStore((s) => s.randomizeConfiguration);

  const exportCurrentJson = () => {
    const data = buildExportJson();
    const blob = new Blob([JSON.stringify(data, null, 2)], {
      type: "application/json",
    });
    downloadBlob(`${data.name}.json`, blob);
  };

  const exportCurrentPng = () => {
    const dataUrl = captureCanvasPng();
    if (!dataUrl) return;
    const a = document.createElement("a");
    a.href = dataUrl;
    a.download = `struktur_${currentType}_${Date.now()}.png`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
  };

  return (
    <div className="flex h-[100dvh] w-full overflow-hidden bg-white">
      {/* LEFT (desktop / tablet) */}
      <aside className={`hidden h-full shrink-0 flex-col border-r bg-card/50 transition-all duration-300 md:flex ${showUI ? "w-64" : "w-0 opacity-0 overflow-hidden border-none"}`}>
        <div className="border-b px-3 py-2">
          <h1 className="font-mono text-[11px] tracking-tight uppercase">
            TRIXIG Generativ
          </h1>
        </div>

        <div className="flex-1 space-y-3 overflow-y-auto p-3">
          <div className="space-y-1.5">
            <span className="text-[10px] uppercase tracking-wider text-muted-foreground font-bold">
              Visning
            </span>
            <div className="grid grid-cols-2 gap-1">
              <Button
                variant={cameraMode === "perspective" ? "secondary" : "outline"}
                size="sm"
                className="h-7 px-1 text-[10px]"
                onClick={() => setCameraMode("perspective")}
              >
                Perspektiv
              </Button>
              <Button
                variant={cameraMode === "orthographic" ? "secondary" : "outline"}
                size="sm"
                className="h-7 px-1 text-[10px]"
                onClick={() => setCameraMode("orthographic")}
              >
                Ortografisk
              </Button>
            </div>
            <Button
              variant="outline"
              size="sm"
              className="h-8 w-full gap-2 text-[10px]"
              onClick={randomize}
              title="Tilfeldig (Q)"
            >
              <RefreshCw className="h-3.5 w-3.5" />
              Generer tilfeldig (Q)
            </Button>
          </div>

          <Separator />
          <ComponentTransformPanel which="motor" />
          <ComponentTransformPanel which="battery" />
        </div>

        <div className="grid grid-cols-3 gap-1 border-t p-2">
          <Button
            onClick={() => setSaveOpen(true)}
            size="icon"
            className="h-9 w-full"
            title="Lagra"
          >
            <Save className="h-4 w-4" />
          </Button>
          <Button
            onClick={exportCurrentJson}
            variant="outline"
            size="icon"
            className="h-9 w-full"
            title="JSON"
          >
            <Download className="h-4 w-4" />
          </Button>
          <Button
            onClick={exportCurrentPng}
            variant="outline"
            size="icon"
            className="h-9 w-full"
            title="PNG"
          >
            <ImageIcon className="h-4 w-4" />
          </Button>
        </div>
      </aside>

      {/* MAIN */}
      <div className="relative flex-1">
        <Scene3D />

        {/* Top floating bar */}
        <div className="pointer-events-none absolute inset-x-0 top-0 flex items-start justify-between p-2 sm:p-3">
          <div className={`pointer-events-auto md:hidden ${showUI ? "" : "hidden"}`}>
            <div className="rounded-md bg-white/80 px-2 py-1 font-mono text-[10px] backdrop-blur-sm border border-slate-200">
              TRIXIG Generativ
            </div>
          </div>

          <div className="pointer-events-auto ml-auto flex items-center gap-1.5">
            {/* Mobile-only actions */}
            <Button
              onClick={() => setSaveOpen(true)}
              variant="outline"
              size="icon"
              className="h-9 w-9 bg-white/80 backdrop-blur-sm md:hidden border-slate-200"
              title="Lagra"
            >
              <Save className="h-4 w-4" />
            </Button>

            <Sheet open={menuOpen} onOpenChange={setMenuOpen}>
              <SheetTrigger asChild>
                <Button
                  variant="outline"
                  size="icon"
                  className={`relative h-9 w-9 bg-white/80 backdrop-blur-sm lg:hidden border-slate-200 ${showUI ? "" : "hidden"}`}
                  title="Lagra"
                >
                  <Menu className="h-4 w-4" />
                  {savedConfigurations.length > 0 && (
                    <span className="absolute -right-1 -top-1 flex h-4 w-4 items-center justify-center rounded-full bg-slate-900 text-[9px] text-white">
                      {savedConfigurations.length}
                    </span>
                  )}
                </Button>
              </SheetTrigger>
              <SheetContent side="right" className="w-72">
                <SheetHeader>
                  <SheetTitle className="text-xs uppercase tracking-widest font-mono">
                    Lagra variantar
                  </SheetTitle>
                </SheetHeader>
                <div className="mt-4 overflow-y-auto">
                  <SavedList />
                </div>
              </SheetContent>
            </Sheet>
          </div>
        </div>

        {/* Mobile-only bottom bar */}
        <div className={`pointer-events-none absolute inset-x-0 bottom-0 z-20 md:hidden ${showUI ? "" : "hidden"}`}>
          <div className="pointer-events-auto bg-gradient-to-t from-white/95 via-white/80 to-transparent pb-[env(safe-area-inset-bottom)]">
            <div className="flex items-center gap-2 px-3 py-3">
              <div className="flex-1 flex items-center justify-center gap-2 bg-slate-900 rounded-xl p-1 shadow-lg">
                <Button
                  onClick={randomize}
                  variant="ghost"
                  size="sm"
                  className="h-10 flex-1 gap-2 text-[11px] font-bold text-white hover:bg-slate-800"
                >
                  <RefreshCw className="h-4 w-4" />
                  TILFELDIG
                </Button>
                <div className="w-px h-5 bg-slate-700" />
                <Button
                  onClick={() => setSaveOpen(true)}
                  variant="ghost"
                  size="sm"
                  className="h-10 flex-1 gap-2 text-[11px] font-bold text-white hover:bg-slate-800"
                >
                  <Save className="h-4 w-4" />
                  LAGRA
                </Button>
              </div>

              <Button
                onClick={exportCurrentPng}
                variant="outline"
                size="icon"
                className="h-12 w-12 shrink-0 bg-white shadow-md rounded-xl border-slate-200"
                title="PNG"
              >
                <ImageIcon className="h-5 w-5" />
              </Button>
            </div>
          </div>
        </div>

        {/* Mobile slide-up sliders for selected component */}
        <MobileTransformSheet />
      </div>

      {/* RIGHT (large desktop) */}
      <aside className={`hidden h-full shrink-0 flex-col border-l bg-card/50 transition-all duration-300 lg:flex ${showUI ? "w-72" : "w-0 opacity-0 overflow-hidden border-none"}`}>
        <div className="flex items-center justify-between border-b px-3 py-2">
          <FolderOpen className="h-3.5 w-3.5 text-muted-foreground" />
          <span className="font-mono text-[10px] text-muted-foreground uppercase tracking-wider">
            Lagra {savedConfigurations.length}
          </span>
        </div>
        <div className="flex-1 overflow-y-auto p-2">
          <SavedList />
        </div>
      </aside>

      <SaveDialog open={saveOpen} onOpenChange={setSaveOpen} />
    </div>
  );
}
