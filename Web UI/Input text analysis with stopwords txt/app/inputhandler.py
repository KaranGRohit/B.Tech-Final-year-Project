
import os

N_SAMPLES = 3
FILENAME = 0
TITLE = 1
samples = [("Error!", "Error!"),
           ("moby-dick.txt", "Moby Dick novel"),
           ("marinetti.txt", "Marinetti poems"),
           ("urteil.txt", "Das Urteil novel"),
           ]

def getSampleText(sampleID):

    if sampleID < 0 or sampleID > N_SAMPLES:
        return (samples[0][0])
        
    filename = samples[sampleID][FILENAME]

    path = os.path.join("app/static/", filename)
    file = open(path, 'r', encoding="utf-8")
    
    return (file.read(), samples[sampleID][TITLE]) 


def readStopwords(language):

    filename = "stopwords" + language + ".txt"
    path = os.path.join("app/static/", filename)
    file = open(path, 'r')
    return file.read().splitlines()  # splitlines is used to remove newlines
