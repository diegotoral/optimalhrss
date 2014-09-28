# -*- encoding: utf-8 -*-

import re


def invalid_elements(l):
    """
    Verifica se uma determinada string é válida ou não, no contexto do parser.

    :param l: String para ser analisada.
    :returns: bool -- Se a string é um dos elementos especiais.
    """
    match = re.match(ur'(\n|\r|-*(\r\n|\r|\n))', l)
    return l != '' and match == None
    # l = l.rstrip('\r\n')
    # hr = ('-' * 79) + '\r\n'
    # return l != '' and l != hr and l != '\r\n' and l != '\n'


class Parser:
    """
    Extrai `HRSSInstances` a partir de descrições em texto.
    """
    def __init__(self):
        self.instances = []
        self.current_instance = None

    def feed(self, lines):
        """
        Alimenta o parser com informações de instâncias.

        As informações sobre as instâncias alimentam o parser que, por sua vez,
        devolve objetos do tipo :class: `HRSSInstance`.

        :param lines: As linhas do arquivo de intâncias.
        :returns: list -- As instâncias carregadas.
        """
        if not lines:
            return False

        lines = filter(invalid_elements, lines)

        while len(lines) > 0:
            self.current_instance = HRSSInstance()
            self.instances.append(self.current_instance)
            self._parse_block(lines)

        return self.instances

    def _parse_block(self, block):
        self._parse_jobs_number(block[0])
        self._parse_machines_number(block.pop(0))
        self._parse_initialization_time(block.pop(0))
        self._parse_setup_times(block.pop(0))
        self._parse_processing_times(block.pop(0))

    def _parse_jobs_number(self, line):
        match = re.match('.*Number of jobs: ([0-9]+)', line)
        if match is None:
            return
        self.current_instance.jobs_number = int(match.group(1))

    def _parse_machines_number(self, line):
        match = re.match('.*Number of machines: ([0-9]+)', line)
        if match is None:
            return
        self.current_instance.machines_number = int(match.group(1))

    def _parse_initialization_time(self, line):
        match = re.match('Initialization time: ([0-9]+)', line)
        if match is None:
            return
        self.current_instance.initialization_time = int(match.group(1))

    def _parse_setup_times(self, line):
        match = re.search('Setup times: ', line)
        if match is None:
            return
        self.current_instance.setup_times = self._get_times('Setup times: ', line)

    def _parse_processing_times(self, line):
        match = re.match('Processing times: ', line)
        if match is None:
            return
        self.current_instance.processing_times = self._get_times('Processing times: ', line)

    def _get_times(self, pattern, line):
        line = line.replace('\r\n', '')
        line = line.replace(pattern, '')
        times = line.split(' ')
        times = filter(lambda l: l != '', times)
        return [int(t) for t in times if t != '']


class HRSSInstance:
    """
    Uma instância de problema HRSS.
    """
    def __init__(self, initialization_time=0, machines_number=0, setup_times=None,
        processing_times=None, jobs_number=0):
        self.jobs_number = jobs_number
        self.initialization_time = initialization_time
        self.machines_number = machines_number
        self.setup_times = setup_times
        self.processing_times = processing_times
