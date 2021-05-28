from unittest import TestCase


class CarroTestCase(TestCase):
    def test_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)


    def test_acelerar(self):
        motor = Motor()
        self.assertEqual(1, motor.velocidade)    
