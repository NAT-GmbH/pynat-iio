import nat


# Create radio
sdr = nat.nat_amc_zynqup_sdr8(uri="ip:192.168.1.160")

# Configure properties
sdr.rx_enabled_channels = [0, 1, 2, 3, 4, 5, 6, 7]
sdr.tx_enabled_channels = [0]
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


sdr.dds_single_tone(1000000, 1, 0)


# Configure DDS
#sdr.dds_enabled = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#sdr.dds_frequencies = [20000000, 0, 20000000, 0, 20000000, 0, 20000000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#sdr.dds_scales = [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#sdr.dds_phases = [0, 0, 90000, 0, 0, 0, 90000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
