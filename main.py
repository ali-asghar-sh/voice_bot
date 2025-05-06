from kokoro import KPipeline
from IPython.display import display, Audio
import soundfile as sf
import torch



pipeline = KPipeline(lang_code='a')
text = '''
I am an expert in AI and robotics education, passionate about creating hands-on, STEM-rich experiences for K–12 learners. As the founder of Duck Learning,I design engaging lessons and projects using tools like LEGO SPIKE Prime, Quarky, and Pictoblox. I’m also a teacher educator,conducting professional development to equip educators with future-ready STEM skills.I manage major robotics competitions in Singapore, including NRC, FLL, and GRG, and have been honoured to serve as a Judge at FIRST Global, an international robotics competition. My mission is to make AI and robotics accessible, meaningful, and inspiring for both students and teachers.
'''
generator = pipeline(text, voice='jf_nezumi')
for i, (gs, ps, audio) in enumerate(generator):
    print(i, gs, ps)
    display(Audio(data=audio, rate=24000, autoplay=i==0))
    sf.write(f'{i}.wav', audio, 24000)
