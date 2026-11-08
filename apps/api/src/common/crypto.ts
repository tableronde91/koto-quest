import { createHash, randomBytes } from 'crypto';

export const newToken = () => randomBytes(32).toString('base64url');
/** Les jetons (session, réinitialisation) ne sont stockés qu'après hachage SHA-256. */
export const hashToken = (token: string) => createHash('sha256').update(token).digest('hex');
