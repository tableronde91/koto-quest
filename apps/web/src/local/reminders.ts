import type { QueryClient } from '@tanstack/react-query';
import { tickReminders } from './backend';

/**
 * Version hors ligne : les défis sont planifiés par l'onglet ouvert (pas de serveur).
 * Si l'onglet est en arrière-plan et que le navigateur l'autorise, une notification système s'affiche ;
 * sinon le défi apparaît en fenêtre dès que l'on revient sur Koto Quest.
 */
export function startLocalReminders(qc: QueryClient) {
  const run = () => {
    let created: ReturnType<typeof tickReminders> = null;
    try {
      created = tickReminders();
    } catch {
      return;
    }
    if (!created) return;
    qc.invalidateQueries({ queryKey: ['inbox'] });
    qc.invalidateQueries({ queryKey: ['dashboard'] });
    if (document.hidden && 'Notification' in window && Notification.permission === 'granted') {
      try {
        const n = new Notification(created.title, { body: created.body, tag: 'koto-challenge' });
        n.onclick = () => {
          window.focus();
          n.close();
        };
      } catch {
        /* certains navigateurs refusent les notifications pour les fichiers locaux */
      }
    }
  };
  run();
  setInterval(run, 30_000);
  document.addEventListener('visibilitychange', () => !document.hidden && run());
}
