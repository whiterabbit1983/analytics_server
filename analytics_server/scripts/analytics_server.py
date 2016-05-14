import cherrypy


from ..services import AnalyticsService


def run():
    conf = {
        '/': {
            'tools.sessions.on': True,
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')]
        }
    }
    cherrypy.config.update({'server.socket_port': 9090})
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(AnalyticsService(), '/', conf)


if __name__ == '__main__':
    run()
