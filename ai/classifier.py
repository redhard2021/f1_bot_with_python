from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

intention = {
    "next_race": [
        "¿Cuándo es la próxima carrera?",
        "Horarios de la próxima carrera",
        "Hora carrera",
        "A qué hora es la próxima carrera",
        "Decime la próxima fecha de F1"
    ],
    "driver_standings": [
        "¿Cómo va el campeonato de pilotos?",
        "¿Cómo van los pilotos?",
        "Tabla de posiciones",
        "Driver standings",
    ],
    "colapinto": [
        "corre Colapa?",
        "Colapinto",
        "Colapinto standings",
        "Colapinto driver standings",
        "Colapinto campeonato"
    ],
}

def classify_intention(user_phrase: str) -> str:
    embedding_phrase = model.encode(user_phrase, convert_to_tensor=True)

    best_similarity = None
    most_similarity = -1

    for key, examples in intention.items():
        for example in examples:
            embedding_example = model.encode(example, convert_to_tensor=True)
            similarity = util.cos_sim(embedding_phrase, embedding_example).item()

            if similarity > most_similarity:
                most_similarity = similarity
                best_similarity = key

    return best_similarity if best_similarity is not None else ""