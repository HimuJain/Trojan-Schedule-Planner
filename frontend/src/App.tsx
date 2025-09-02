import { useEffect, useState } from "react";
import type { Course } from "./lib/types";
import { fetchCourses } from "./lib/api";
import { useCourseBin } from "./state/useBin";
function CourseCard(
  { c, inBin, onAdd, onRemove }:
  { c: Course; inBin: boolean; onAdd: (c: Course) => void; onRemove: (code: string) => void }
) {
  return (
    <div className="card p-4">
      <div className="font-semibold text-lg">{c.code} · {c.title}</div>
      <div className="text-sm text-neutral-600 dark:text-neutral-400 mt-1">
        {c.dept} · {c.units} units · {c.days.join(', ')} {c.time} · {c.location}
      </div>
      <div className="flex gap-2 mt-2 flex-wrap">
        {c.ge.map(g => <span key={g} className="badge">{g}</span>)}
      </div>

      <button
        className="btn mt-3"
        onClick={() => (inBin ? onRemove(c.code) : onAdd(c))}
        title={inBin ? "Remove from bin" : "Add to bin"}
      >
        {inBin ? "Remove" : "Add to Bin"}
      </button>
    </div>
  );
}
// function useLocalStorage<T>(key: string, initial: T) {
//   const [val, setVal] = useState<T>(() => {
//     const raw = localStorage.getItem(key);
//     return raw ? (JSON.parse(raw) as T) : initial;
//   });
//   useEffect(() => { localStorage.setItem(key, JSON.stringify(val)); }, [key, val]);
//   return [val, setVal] as const;
// }

export default function App() {
  const [q, setQ] = useState("");
  const [courses, setCourses] = useState<Course[]>([]);

  useEffect(() => {
  const id = setTimeout(() => {
    fetchCourses(q).then(setCourses).catch(console.error);
  }, 150);
  return () => clearTimeout(id);
  }, [q]);


  const { bin, add, remove, clear, units, over18, isInBin } = useCourseBin();

  return (
    <div className="container py-8">
      <header className="mb-6">
        <h1 className="text-2xl font-bold tracking-tight">Trojan Schedule Planner(MVP)</h1>
        <p className="text-sm text-neutral-600 dark:text-neutral-400">Search, add to bin, and review quickly.</p>
      </header>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <section>
          <div className="flex items-center gap-3 mb-3">
            <input className="input" placeholder="Search by code/title/dept…" value={q} onChange={e => setQ(e.target.value)} />
          </div>
          <div className="space-y-3">
            {courses.map(c => {
              return (
                <CourseCard
                  key={c.code}
                  c={c}
                  inBin={isInBin(c.code)}
                  onAdd={() => add(c)}          
                  onRemove={() => remove(c.code)} 
                />
              );
            })}
          </div>
        </section>

        <section>
          <div className="card p-4">
            <h2 className="text-lg font-semibold">Course Bin</h2>
            {bin.length === 0 && <div className="text-sm text-neutral-600 dark:text-neutral-400 mt-2">No courses yet. Add some →</div>}
            <ul className="divide-y divide-neutral-200 dark:divide-neutral-800 mt-2">
              {bin.map(c => (
                <li key={c.code} className="py-2 flex items-center justify-between">
                  <div><span className="font-medium">{c.code}</span> <span className="text-neutral-600 dark:text-neutral-400">{c.title}</span></div>
                  <button className="btn" onClick={() => remove(c.code)}>Remove</button>
                </li>
              ))}
            </ul>
            <div>Subtotal: {units} {over18 && <span>Over 18</span>}</div>
          </div>
        </section>
      </div>
    </div>
  )
}