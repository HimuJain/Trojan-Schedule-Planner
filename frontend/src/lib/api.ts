import type { Course } from "./types";
// export const API_BASE = "/api";


export async function fetchCourses(q: string = ""): Promise<Course[]> {
  const qs = q ? `?q=${encodeURIComponent(q)}` : "";
  const res = await fetch(`/api/courses${qs}`);
  if (!res.ok) throw new Error("Failed to fetch courses");
  return res.json();
}