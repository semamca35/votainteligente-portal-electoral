# coding=utf-8
from collections import OrderedDict

WHEN_CHOICES = [
    ('', u'Selecciona cuándo'),
    ('1_year', u'1 año'),
    ('2_year', u'2 años'),
    ('3_year', u'3 años'),
    ('4_year', u'4 años'),
]

TOPIC_CHOICES = (('', u'Selecciona una categoría'),
                 ('asistencia', u'Asistencia y protección social'),
                 ('ciencias', u'Ciencias'),
                 ('cultura', u'Cultura'),
                 ('deporte', u'Deporte'),
                 ('derechoshumanos', u'Derechos Humanos'),
                 ('derechos', u'Derechos Sociales'),
                 ('emergencia', u'Desastres Naturales'),
                 ('economia', u'Economía'),
                 ('educacion', u'Educación'),
                 ('empleo', u'Empleo'),
                 ('energia', u'Energía'),
                 ('genero', u'Equidad y género'),
                 ('diversidad', u'Inclusión'),
                 ('infancia', u'Infancia y juventud'),
                 ('justicia', u'Justicia'),
                 ('medioambiente', u'Medio ambiente'),
                 ('medios', u'Medios de comunicación'),
                 ('migracion', u'Migración'),
                 ('mineria', u'Minería'),
                 ('pensiones', u'Pensiones'),
                 ('participacion', u'Participación'),
                 ('prevision', u'Previsión'),
                 ('proteccionsocial', u'Protección social'),
                 ('pueblosoriginarios', u'Pueblos originarios'),
                 ('recursosnaturales', u'Recursos naturales'),
                 ('salud', u'Salud'),
                 ('seguridad', u'Seguridad'),
                 ('sustentabilida', u'Sustentabilidad'),
                 ('terceraedad', u'Tercera Edad'),
                 ('trabajo', u'Trabajo'),
                 ('transparencia', u'Transparencia'),
                 ('transporte', u'Transporte'),
                 ('espaciospublicos', u'Urbanismo y Espacios públicos'),
                 )

TEXTS = OrderedDict({
    'problem': {'label': u'El problema que se quiere solucionar es',
                'preview_question': u'¿Cuál es el problema que quieres solucionar?',
                'help_text': u'Contaminación en la ciudad',
                'placeholder': u'Escribe el problema que quieres solucionar con tu propuesta.',
                },
    'causes': {'label': u'La causa de este problema es',
               'preview_question': u'Cuáles son las causas de este problema?',
               'placeholder': u'Escribe aquí la causa de tu problema que quieres abordar. Recuerda solo escribir una.',
               'long_text': "causes_help.html"},
    'solution': {'label': u'¿Cuáles posibles soluciones creemos que existen para pasar del problema a la situación ideal?',
                 'preview_question': u'¿Cual sería la situación ideal?',
                 'help_text': u'',
                 'placeholder': u'Escribe aquí la situación ideal a la que quieres llegar.',
                 'long_text': "paso3.html"},
    'solution_at_the_end': {'label': u'La propuesta para solucionar este problema es',
                            'preview_question': u'¿Cuál sería la solución?',
                            'help_text': u'Se puede regular el uso de bolsas plásticas en los supermercados a solo tres por persona, las otras bolsas que se usen deben ser reutilizables.',
                            'placeholder': u'Escribe aquí la solucion para el problema que definiste.'},
    'when': {'label': u'Tiempo en el cual se puede llevar a cabo la propuesta',
             'preview_question': u'¿Cuándo debería estar esto listo?',
             'help_text': u'1 año',
             'placeholder': u'',},
    'title': {'label': u'Colócale título',
              'preview_question': u'Título',
              'help_text': u'',
              'placeholder': u'Título de la propuesta',
              'long_text': ""},
    'clasification': {'label': u'Selecciona una categoría',
                      'preview_question': u'Clasificación',
                      'help_text': u'Medio Ambiente',
                      'placeholder': u'',
                      'long_text': ""},
    'is_local_meeting': {'label': u'¿Esta propuesta es producto de un encuentro local?',
                      'preview_question': u'¿Es un encuentro local?',
                      'help_text': u'',
                      'placeholder': u'',
                      'long_text': "is_local_meeting.html"},
    'generated_at': {'label': u'¿En qué comuna se generó esta propuesta?',
                      'preview_question': u'¿Es un encuentro local?',
                      'help_text': u'Si eres una ONG de vocación nacional, esta opción no aplica',
                      'placeholder': u'',
                      'long_text': "generated_at.html"},
    'terms_and_conditions': {'label': u'Términos y condiciones',
                             'preview_question': u'',
                             'help_text': u'',
                             'placeholder': u'',
                             'long_text': "terms_and_conditions.html"},
    'is_testing': {'label': u'Esta propuesta es de prueba',
                             'preview_question': u'',
                             'help_text': u'Sólo la podrás ver tu y nosotros podremos borrarlas periodicamente.',
                             'placeholder': u'',
                             'long_text': ""},
})

SEARCH_ELEMENTS_FROM_DATA = [
  'problem','solution','causes', 'solution_at_the_end', 'when'
]
