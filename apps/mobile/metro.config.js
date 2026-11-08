// Monorepo : Expo détecte les espaces de travail npm et surveille les paquets partagés.
const { getDefaultConfig } = require('expo/metro-config');
module.exports = getDefaultConfig(__dirname);
