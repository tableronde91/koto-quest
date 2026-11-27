# Contes : place de la bonne réponse. Les questions sont rédigées avec la bonne réponse en premier ;
# mix() la déplace à une position stable (calculée d'après le chapitre), pour qu'elle ne soit pas toujours le premier choix.
def mix(stories):
    for s in stories:
        if any(q['answer'] != 0 for c in s['chapters'] for q in c['questions']):
            continue  # conte dont les réponses ont déjà été placées à la main
        for c in s['chapters']:
            seed = sum(ord(ch) for ch in c['slug'])
            for i, q in enumerate(c['questions']):
                pos = (seed + 2 * i) % len(q['choices'])
                q['choices'][0], q['choices'][pos] = q['choices'][pos], q['choices'][0]
                q['answer'] = pos
    return stories
