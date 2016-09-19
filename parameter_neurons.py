import Inh_Exc_Neurons

dict_parameters_inh = {"E_L": -70.0, "C_m": 250.0, "tau_m": 10.0, "t_ref": 2.0, "V_th": -55.0, "V_reset": -70.0, "tau_syn":  2.0, "I_e": 370.0}
dict_parameters_exc = {"E_L": -70.0, "C_m": 250.0, "tau_m": 20.0, "t_ref": 2.0, "V_th": -55.0, "V_reset": -70.0, "tau_syn":  2.0, "I_e": 220.0}

d = 1.0
Je = 2.0
Ke = 20
Ji = -4.0
Ki = 12

neuron_population = 100
simulation_time = 250.0

Inh_Exc_Neurons.random_neuron_generator(Inh_Exc_Neurons.exc_neuron_parameters(dict_parameters_exc, neuron_population), Inh_Exc_Neurons.inh_neuron_parameters(dict_parameters_inh, neuron_population), simulation_time, d, Je, Ke, Ji, Ki, dict_parameters_inh, dict_parameters_exc)
