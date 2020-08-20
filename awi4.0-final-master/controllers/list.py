import web
import database.conection as personas

model_personas = personas.Personas()

template = web.template.render("views/", base="template2")

class List:
    def GET(self):
        try:
            result = model_personas.select()
            return template.SelectAll(result)
        except Exception as e:
            return "Error: "+str(e)
