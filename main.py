from fastapi import FastAPI
app = FastAPI()


# @app.get("/cc/{cc}")
# async def read_item(cc):
#     return {"cc": cc}


# @app.get("/nlp/")
# async def read_doc(text):
#     doc = nlp(text)
#     return {"ents": [{'ent_name': ent.kb_id_.split('/')[-1].replace('_', ' ')} for ent in doc.ents]}


@app.get("/")
async def root():
    return {"message": "Hello Urgence World"}


@app.get("/help/")
async def help():
    with open('help.txt') as f:
        lines = f.readlines()
    return {"text": lines}
