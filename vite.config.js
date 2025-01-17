import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  base: '/static/react/dist/', // Assurez-vous que cela correspond au chemin Django
  build: {
    outDir: './ProjetInfoCIR3/static/react/dist', // Place les fichiers dans le bon dossier Django
    assetsDir: 'assets', // Répertoire pour les fichiers CSS/JS/images
  },
});
