# coding=utf-8
from elections.models import Area
from merepresenta.models import Partido, Coaligacao, Candidate
from tse_data_importer.csv_reader import CsvReader
from tse_data_importer.importer import RowsReaderAdapter
from django.conf import settings
from datetime import datetime

def output_logger(self, msg):
    print msg

class TSEProcessorMixin(object):
    output_logger_func = output_logger

    def gender_definer(self, gender):
        if gender == 'FEMININO':
            return "F"
        if gender == 'MASCULINO':
            return "M"
        return ""

    def process_candidate(self, candidate_dict, election, partido):
        gender = self.gender_definer(candidate_dict['gender'])
        try:
            data_de_nascimento = datetime.strptime(candidate_dict['date_of_birth'], "%d/%m/%Y").date()
        except:
            data_de_nascimento = None
        candidate, created = Candidate.objects.get_or_create(name=candidate_dict['nome'],
                                                             nome_completo=candidate_dict['nome_completo'],
                                                             numero=candidate_dict['number'],
                                                             cpf=candidate_dict['cpf'],
                                                             data_de_nascimento=data_de_nascimento,
                                                             race=candidate_dict['race'],
                                                             original_email=candidate_dict['mail'],
                                                             email_repeated=candidate_dict['email_repeated'],
                                                             gender=gender)
        election.candidates.add(candidate)
        candidate.partido = partido
        candidate.save()

        return candidate

    def do_something(self, row):
        
        result = {}
        if settings.FILTERABLE_AREAS_TYPE:
            state_classification = settings.FILTERABLE_AREAS_TYPE[0]
        else:
            state_classification = 'state'
        area, created = Area.objects.get_or_create(identifier=row['area']['slug'], name=row['area']['area_name'], classification=state_classification)
        result['area'] = area
        election, created = area.elections.get_or_create(name=row['area']['election_name'])
        result['election'] = election
        coaligacao, created = Coaligacao.objects.get_or_create(name=row['coaligacao']['name'],
                                                               number=row['coaligacao']['number'])
        result['coaligacao'] = coaligacao
        partido, created = Partido.objects.get_or_create(name=row['partido']['name'],
                                                         initials=row['partido']['initials'],
                                                         number=row['partido']['number'],
                                                         coaligacao=coaligacao)
        result['partido'] = partido
        row['candidate']['email_repeated'] = row['email_repeated']

        result['candidate'] = self.process_candidate(row['candidate'], election, partido)
        self.output_logger_func("imported %s de %s" % (result['candidate'].name, area.name))
        return result

class TSEProcessor(TSEProcessorMixin, CsvReader):
    pass