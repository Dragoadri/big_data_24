from mrjob.job import MRJob
from mrjob.step import MRStep
import json

class WordJsonCounter(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   combiner=self.combiner,
                   reducer=self.reducer),
            MRStep(reducer=self.reducer_sorter)
        ]

    def mapper(self, _, line):
        # Lee cada linea del archivo JSON y extrae el texto
        try:
            data = json.loads(line)
            text = data.get("review_text", "")
            words = text.split()

            for word in words:
                yield word.lower(), 1
        except Exception as e:
            pass  # Ignora lineas que no se puedan procesar

    def combiner(self, word, counts):
        # Sumar las ocurrencias de las palabras localmente
        yield word, sum(counts)

    def reducer(self, word, counts):
        # Sumar las ocurrencias de las palabras globalmente
        yield None, (sum(counts), word)

    def reducer_sorter(self, _, word_counts):
        # Ordenar las palabras por frecuencia en orden descendente
        for count, word in sorted(word_counts, reverse=True):
            yield word, count

if __name__ == "__main__":
    WordJsonCounter.run()
