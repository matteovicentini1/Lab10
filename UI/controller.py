import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        if self._view._txtAnno.value=='':
            self._view.create_alert('Inserire anno')
        else:
            try:
                anno = int(self._view._txtAnno.value)
                if anno>=1816 and anno <=2016:
                    self._view._txt_result.controls.clear()
                    self._model.creagrafo(anno)
                    stsati=self._model.elencostati()
                    self._view._txt_result.controls.append(ft.Text('grafo creato correttamente'))
                    self._view._txt_result.controls.append(ft.Text(f'Nodi - {self._model.getnodi()}'))
                    self._view._txt_result.controls.append(ft.Text(f'Archi - {self._model.getarchi()}'))
                    self._view._txt_result.controls.append(ft.Text(f'il grafo ha {self._model.getconnesse()} componenti connesse'))
                    self._view._txt_result.controls.append(ft.Text('Di seguito il dettaglio dei nodi:'))
                    for i in (stsati):
                        self._view._txt_result.controls.append(ft.Text(f'{i[0].StateAbb} -- {i[1]} vicini'))
                    self._view.connessionistato.disabled=False
                    self.filldrop()
                    self._view.update_page()
                else:
                    self._view.create_alert('Anno fuori dal range')
            except ValueError:
                self._view.create_alert('Anno nel formato sbagiato')

    def filldrop(self):
        for i in self._model.grafo.nodes():
            self._view.ddstato.options.append(ft.dropdown.Option(key=i.CCode,text=i.StateAbb))

    def cercaconn(self,e):
        if self._view.ddstato.value is None:
            self._view.create_alert('Inserire uno stato')
        else:
            self._view._txt_result.controls.clear()
            stato = self._view.ddstato.value
            raggiungibili = self._model.raggiungibili(int(stato))
            for i in raggiungibili:
                self._view._txt_result.controls.append(ft.Text(f'{i.StateAbb}'))
            self._view.update_page()
