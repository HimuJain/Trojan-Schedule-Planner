import { useEffect, useMemo, useState, useCallback } from "react";
import type { Course } from "../lib/types";

const LS_KEY = "uscplanner.bin.v1";

export function useCourseBin() {
  const [bin, setBin] = useState<Course[]>(() => {
    try { return JSON.parse(localStorage.getItem(LS_KEY) ?? "[]"); } catch { return []; }
  });
  useEffect(() => { localStorage.setItem(LS_KEY, JSON.stringify(bin)); }, [bin]);

  const add = (c: Course) =>
    setBin(prev => (prev.some(x => x.code === c.code) ? prev : [...prev, c]));
  const remove = (code: string) =>
    setBin(prev => prev.filter(x => x.code !== code));

  const binCodes = useMemo(() => new Set(bin.map(b => b.code)), [bin]);

  const isInBin = useCallback((code: string) => binCodes.has(code), [binCodes]);


  const clear = useCallback(() => setBin([]), []);

  const units = useMemo(() => bin.reduce((s, c) => s + c.units, 0), [bin]);
  const over18 = units > 18;

  return { bin, add, remove, clear, units, over18, isInBin };
}
