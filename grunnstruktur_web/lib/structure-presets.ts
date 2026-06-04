export type StructureType =
  | "inline"
  | "parallell"
  | "stablet"
  | "separert"
  | "l-form"
  | "t-form"
  | "over-under"
  | "integrert"
  | "pistol";

export interface StructurePreset {
  id: StructureType;
  number: string;
  name: string;
  description: string;
  motorhus: {
    position: [number, number, number];
    rotation: [number, number, number];
  };
  batteri_pcb: {
    position: [number, number, number];
    rotation: [number, number, number];
  };
}

// Posisjonar i mm (vert skalert ned i scenen).
export const structurePresets: StructurePreset[] = [
  {
    id: "inline",
    number: "01",
    name: "Inline",
    description: "Motor og batteri ligg på same akse.",
    motorhus: { position: [0, 0, 0], rotation: [0, 0, 0] },
    batteri_pcb: { position: [-90, 0, 0], rotation: [0, 0, 0] },
  },
  {
    id: "parallell",
    number: "02",
    name: "Parallell",
    description: "Motor og batteri ligg side om side.",
    motorhus: { position: [0, 0, 0], rotation: [0, 0, 0] },
    batteri_pcb: { position: [0, 0, 45], rotation: [0, 0, 0] },
  },
  {
    id: "stablet",
    number: "03",
    name: "Stabla",
    description: "Ein komponent ligg over den andre.",
    motorhus: { position: [0, 0, 0], rotation: [0, 0, 0] },
    batteri_pcb: { position: [0, 40, 0], rotation: [0, 0, 0] },
  },
  {
    id: "separert",
    number: "04",
    name: "Separert",
    description: "Funksjonelt kopla, men fysisk skilde.",
    motorhus: { position: [0, 0, 0], rotation: [0, 0, 0] },
    batteri_pcb: { position: [-130, -40, 30], rotation: [0, 0, 0] },
  },
  {
    id: "l-form",
    number: "05",
    name: "L-form",
    description: "Motor horisontalt, batteri/PCB dannar grep.",
    motorhus: { position: [0, 0, 0], rotation: [0, 0, 0] },
    batteri_pcb: { position: [-40, -55, 0], rotation: [0, 0, -90] },
  },
  {
    id: "t-form",
    number: "06",
    name: "T-form",
    description: "Batteri/PCB vinkelrett under motorhuset.",
    motorhus: { position: [0, 0, 0], rotation: [0, 0, 0] },
    batteri_pcb: { position: [-15, -55, 0], rotation: [0, 0, -90] },
  },
  {
    id: "over-under",
    number: "07",
    name: "Over-under",
    description: "Motor over batteri/PCB i kompakt kapsling.",
    motorhus: { position: [0, 20, 0], rotation: [0, 0, 0] },
    batteri_pcb: { position: [-15, -20, 0], rotation: [0, 0, 0] },
  },
  {
    id: "integrert",
    number: "08",
    name: "Integrert",
    description: "Komponentane pakka tett innanfor same ytre volum.",
    motorhus: { position: [0, 5, 0], rotation: [0, 0, 0] },
    batteri_pcb: { position: [-25, -10, 0], rotation: [0, 0, 0] },
  },
  {
    id: "pistol",
    number: "09",
    name: "Pistol",
    description: "Motor er hovud, batteri/PCB dannar handtak.",
    motorhus: { position: [0, 0, 0], rotation: [0, 0, 0] },
    batteri_pcb: { position: [-25, -60, 0], rotation: [0, 0, -55] },
  },
];

export const evaluationKeys = [
  "kompakt",
  "ergonomi",
  "kapsling",
  "batteritilgang",
  "silhuett",
] as const;
export type EvaluationKey = (typeof evaluationKeys)[number];
export const evaluationLabels: Record<EvaluationKey, string> = {
  kompakt: "Kompakt volum",
  ergonomi: "Ergonomisk retning",
  kapsling: "Enkel kapsling",
  batteritilgang: "Batteritilgang",
  silhuett: "TRIXIG-silhuett",
};

export type Evaluation = Partial<Record<EvaluationKey, number>>; // 0-3

export interface SavedConfiguration {
  id: string;
  name: string;
  type: StructureType | "custom";
  motorhus: {
    position: [number, number, number];
    rotation: [number, number, number];
  };
  batteri_pcb: {
    position: [number, number, number];
    rotation: [number, number, number];
  };
  note?: string;
  evaluation?: Evaluation;
  thumbnail?: string;
  saved: string;
}
