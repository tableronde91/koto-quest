import { Platform } from 'react-native';

/**
 * Adresse de l'API. À définir avec EXPO_PUBLIC_API_URL (ex. http://192.168.1.20:3000 pour un
 * téléphone sur le même Wi-Fi). Par défaut : l'émulateur Android voit l'ordinateur en 10.0.2.2.
 */
export const API_URL = (process.env.EXPO_PUBLIC_API_URL ?? (Platform.OS === 'android' ? 'http://10.0.2.2:3000' : 'http://localhost:3000')).replace(/\/$/, '');
