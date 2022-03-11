import nat

import time
import matplotlib.pyplot as plt
import numpy as np


def measure_phase(chan0, chan1):
    assert len(chan0) == len(chan1)
    errorV = np.angle(chan0 * np.conj(chan1)) * 180 / np.pi
    error = np.mean(errorV)
    return error


# Create radio
sdr = nat.nat_amc_zynqup_sdr8(uri="ip:192.168.1.160")

# Configure properties
sdr.rx_enabled_channels = [0, 1, 2, 3, 4, 5, 6, 7]
sdr.tx_enabled_channels = [0, 1]
sdr.trx_lo = 2000000000
sdr.trx_lo_chip_b = 2000000000
sdr.trx_lo_chip_c = 2000000000
sdr.trx_lo_chip_d = 2000000000
sdr.tx_hardwaregain_chan0 = -10
sdr.tx_hardwaregain_chan1 = -10
sdr.tx_hardwaregain_chan0_chip_b = -10
sdr.tx_hardwaregain_chan1_chip_b = -10
sdr.tx_hardwaregain_chan0_chip_c = -10
sdr.tx_hardwaregain_chan1_chip_c = -10
sdr.tx_hardwaregain_chan0_chip_d = -10
sdr.tx_hardwaregain_chan1_chip_d = -10
sdr.gain_control_mode_chan0 = "slow_attack"
sdr.gain_control_mode_chan1 = "slow_attack"
sdr.gain_control_mode_chan0_chip_b = "slow_attack"
sdr.gain_control_mode_chan1_chip_b = "slow_attack"
sdr.gain_control_mode_chan0_chip_c = "slow_attack"
sdr.gain_control_mode_chan1_chip_c = "slow_attack"
sdr.gain_control_mode_chan0_chip_d = "slow_attack"
sdr.gain_control_mode_chan1_chip_d = "slow_attack"
sdr.rx_buffer_size = 2 ** 17
sdr.dds_single_tone(1000000, 1, 0)


# Read properties
# print("TRX LO %s" % (sdr.trx_lo))
# print("TRX LO %s" % (sdr.trx_lo_chip_b))



#HMC7044 Delay
# sdr.hmc7044_output_delay(0, 0, 100)
# sdr.hmc7044_output_delay(2, 0, 100)
# sdr.hmc7044_output_delay(4, 0, 100)
# sdr.hmc7044_output_delay(6, 0, 100)

# Collect data

fsr = int(sdr.rx_sample_rate)
for r in range(5):
    x = sdr.rx()

    print(F"Try {r}")
    for i in range(8):
        print(F"Diff between RX0 and RX{i}: {measure_phase(x[0], x[i])}")

    plt.clf()
    plt.plot(x[0][:2000].real, label="RX1")
    plt.plot(x[1][:2000].real, label="RX2")
    plt.plot(x[2][:2000].real, label="RX3")
    plt.plot(x[3][:2000].real, label="RX4")
    plt.plot(x[4][:2000].real, label="RX5")
    plt.plot(x[5][:2000].real, label="RX6")
    plt.plot(x[6][:2000].real, label="RX7")
    plt.plot(x[7][:2000].real, label="RX8")

    plt.draw()
    plt.pause(0.05)
    time.sleep(0.1)

plt.show()
