import web
from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')

urls = (
    '/', 'controllers.index.Index',
    '/SelectAll', 'controllers.list.List',
    '/Insertar', 'controllers.insert.Insert',
    '/Borrar/(.*)', 'controllers.delete.Delete',
    '/Actualizar/(.*)', 'controllers.update.Update',
    '/Vista/(.*)', 'controllers.view.ViewPerson'
)
app = web.application(urls, globals())

render = web.template.render("views/", base="template")

if __name__ == "__main__":
    app.run()