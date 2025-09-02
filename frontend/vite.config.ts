import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwind from "@tailwindcss/vite";


// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), tailwind()],
  server: {
    proxy: {
      // Anything starting with /api is forwarded to FastAPI on your box
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        // optional: rewrite if your FastAPI paths don’t include /api
        rewrite: (path) => path.replace(/^\/api/, "")
      },
    },
  },
})