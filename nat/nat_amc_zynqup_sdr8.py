# Copyright (C) 2021 Gesellschaft fuer Netzwerk- und Automatisierungstechnologie m.b.H (N.A.T. GmbH)
# Copyright (C) 2019 Analog Devices, Inc.
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#     - Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     - Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in
#       the documentation and/or other materials provided with the
#       distribution.
#     - Neither the name of N.A.T. GmbH/Analog Devices, Inc. nor the names of its
#       contributors may be used to endorse or promote products derived
#       from this software without specific prior written permission.
#     - The use of this software may or may not infringe the patent rights
#       of one or more patent holders.  This license does not release you
#       from the requirement that you obtain separate licenses from these
#       patent holders to use this software.
#     - Use of the software either in source or binary form, must be run
#       on or directly connected to an N.A.T. GmbH/Analog Devices Inc. component.
#
# THIS SOFTWARE IS PROVIDED BY N.A.T. GmbH/ANALOG DEVICES "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED.
#
# IN NO EVENT SHALL N.A.T. GmbH/ANALOG DEVICES BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, INTELLECTUAL PROPERTY
# RIGHTS, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
# THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import adi
from nat.nat_amc_zynqup_sdr4 import nat_amc_zynqup_sdr4


class nat_amc_zynqup_sdr8(nat_amc_zynqup_sdr4):
    """ NAT-AMC-ZYNQUP-SDR8

    parameters:
        uri: type=string
            URI of context with NAT-AMC-ZYNQUP-SDR
        jesd_monitor: type=boolean
            Boolean flag to enable JESD monitoring. jesd input is
            ignored otherwise.
        jesd: type=adi.jesd
            JESD object associated with NAT-AMC-ZYNQUP-SDR
    """

    _rx_channel_names = [
        "voltage0_i",
        "voltage0_q",
        "voltage1_i",
        "voltage1_q",
        "voltage2_i",
        "voltage2_q",
        "voltage3_i",
        "voltage3_q",
        "voltage4_i",
        "voltage4_q",
        "voltage5_i",
        "voltage5_q",
        "voltage6_i",
        "voltage6_q",
        "voltage7_i",
        "voltage7_q",
    ]
    _tx_channel_names = [
        "voltage0",
        "voltage1",
        "voltage2",
        "voltage3",
        "voltage4",
        "voltage5",
        "voltage6",
        "voltage7",
        "voltage8",
        "voltage9",
        "voltage10",
        "voltage11",
        "voltage12",
        "voltage13",
        "voltage14",
        "voltage15",
    ]
    _device_name = ""

    def __init__(self, uri="", jesd_monitor=False, jesd=None):

        nat_amc_zynqup_sdr4.__init__(self, uri=uri, jesd_monitor=jesd_monitor, jesd=jesd)
        self._ctrl_c = self._ctx.find_device("adrv9009-phy-c")
        self._ctrl_d = self._ctx.find_device("adrv9009-phy-d")

    @property
    def frequency_hopping_mode_chip_c(self):
        """frequency_hopping_mode_chip_c: Set Frequency Hopping Mode"""
        return self._get_iio_attr(
            "TRX_LO", "frequency_hopping_mode", True, self._ctrl_c
        )

    @frequency_hopping_mode_chip_c.setter
    def frequency_hopping_mode_chip_c(self, value):
        self._set_iio_attr(
            "TRX_LO", "frequency_hopping_mode", True, value, self._ctrl_c
        )

    @property
    def frequency_hopping_mode_chip_d(self):
        """frequency_hopping_mode_chip_d: Set Frequency Hopping Mode"""
        return self._get_iio_attr(
            "TRX_LO", "frequency_hopping_mode", True, self._ctrl_d
        )

    @frequency_hopping_mode_chip_d.setter
    def frequency_hopping_mode_chip_d(self, value):
        self._set_iio_attr(
            "TRX_LO", "frequency_hopping_mode", True, value, self._ctrl_d
        )

    @property
    def frequency_hopping_mode_en_chip_c(self):
        """frequency_hopping_mode_en: Enable Frequency Hopping Mode"""
        return self._get_iio_attr(
            "TRX_LO", "frequency_hopping_mode_enable", True, self._ctrl_c
        )

    @frequency_hopping_mode_en_chip_c.setter
    def frequency_hopping_mode_en_chip_c(self, value):
        self._set_iio_attr(
            "TRX_LO", "frequency_hopping_mode_enable", True, value, self._ctrl_c
        )

    @property
    def frequency_hopping_mode_en_chip_d(self):
        """frequency_hopping_mode_en: Enable Frequency Hopping Mode"""
        return self._get_iio_attr(
            "TRX_LO", "frequency_hopping_mode_enable", True, self._ctrl_d
        )

    @frequency_hopping_mode_en_chip_d.setter
    def frequency_hopping_mode_en_chip_d(self, value):
        self._set_iio_attr(
            "TRX_LO", "frequency_hopping_mode_enable", True, value, self._ctrl_d
        )

    @property
    def calibrate_rx_phase_correction_en_chip_c(self):
        """calibrate_rx_phase_correction_en: Enable RX Phase Correction Calibration"""
        return self._get_iio_dev_attr("calibrate_rx_phase_correction_en", self._ctrl_c)

    @calibrate_rx_phase_correction_en_chip_c.setter
    def calibrate_rx_phase_correction_en_chip_c(self, value):
        self._set_iio_dev_attr_str(
            "calibrate_rx_phase_correction_en", value, self._ctrl_c
        )

    @property
    def calibrate_rx_phase_correction_en_chip_d(self):
        """calibrate_rx_phase_correction_en: Enable RX Phase Correction Calibration"""
        return self._get_iio_dev_attr("calibrate_rx_phase_correction_en", self._ctrl_d)

    @calibrate_rx_phase_correction_en_chip_d.setter
    def calibrate_rx_phase_correction_en_chip_d(self, value):
        self._set_iio_dev_attr_str(
            "calibrate_rx_phase_correction_en", value, self._ctrl_d
        )

    @property
    def calibrate_rx_qec_en_chip_c(self):
        """calibrate_rx_qec_en_chip_c: Enable RX QEC Calibration"""
        return self._get_iio_dev_attr("calibrate_rx_qec_en", self._ctrl_c)

    @calibrate_rx_qec_en_chip_c.setter
    def calibrate_rx_qec_en_chip_c(self, value):
        self._set_iio_dev_attr_str("calibrate_rx_qec_en", value, self._ctrl_c)

    @property
    def calibrate_rx_qec_en_chip_d(self):
        """calibrate_rx_qec_en_chip_d: Enable RX QEC Calibration"""
        return self._get_iio_dev_attr("calibrate_rx_qec_en", self._ctrl_d)

    @calibrate_rx_qec_en_chip_d.setter
    def calibrate_rx_qec_en_chip_d(self, value):
        self._set_iio_dev_attr_str("calibrate_rx_qec_en", value, self._ctrl_d)

    @property
    def calibrate_tx_qec_en_chip_c(self):
        """calibrate_tx_qec_en_chip_c: Enable TX QEC Calibration"""
        return self._get_iio_dev_attr("calibrate_tx_qec_en", self._ctrl_c)

    @calibrate_tx_qec_en_chip_c.setter
    def calibrate_tx_qec_en_chip_c(self, value):
        self._set_iio_dev_attr_str("calibrate_tx_qec_en", value, self._ctrl_c)

    @property
    def calibrate_tx_qec_en_chip_d(self):
        """calibrate_tx_qec_en_chip_d: Enable TX QEC Calibration"""
        return self._get_iio_dev_attr("calibrate_tx_qec_en", self._ctrl_d)

    @calibrate_tx_qec_en_chip_d.setter
    def calibrate_tx_qec_en_chip_d(self, value):
        self._set_iio_dev_attr_str("calibrate_tx_qec_en", value, self._ctrl_d)

    @property
    def calibrate_chip_c(self):
        """calibrate_chip_c: Trigger Calibration"""
        return self._get_iio_dev_attr("calibrate", self._ctrl_c)

    @calibrate_chip_c.setter
    def calibrate_chip_c(self, value):
        self._set_iio_dev_attr_str("calibrate", value, self._ctrl_c)

    @property
    def calibrate_chip_d(self):
        """calibrate_chip_d: Trigger Calibration"""
        return self._get_iio_dev_attr("calibrate", self._ctrl_d)

    @calibrate_chip_d.setter
    def calibrate_chip_d(self, value):
        self._set_iio_dev_attr_str("calibrate", value, self._ctrl_d)

    @property
    def rx_quadrature_tracking_en_chan0_chip_c(self):
        """Enable Quadrature tracking calibration for RX1"""
        return self._get_iio_attr("voltage0", "quadrature_tracking_en", False, self._ctrl_c)

    @rx_quadrature_tracking_en_chan0_chip_c.setter
    def rx_quadrature_tracking_en_chan0_chip_c(self, value):
        self._set_iio_attr("voltage0", "quadrature_tracking_en", False, value, self._ctrl_c)

    @property
    def rx_quadrature_tracking_en_chan0_chip_d(self):
        """Enable Quadrature tracking calibration for RX1"""
        return self._get_iio_attr("voltage0", "quadrature_tracking_en", False, self._ctrl_d)

    @rx_quadrature_tracking_en_chan0_chip_d.setter
    def rx_quadrature_tracking_en_chan0_chip_d(self, value):
        self._set_iio_attr("voltage0", "quadrature_tracking_en", False, value, self._ctrl_d)

    @property
    def rx_quadrature_tracking_en_chan1_chip_c(self):
        """Enable Quadrature tracking calibration for RX2"""
        return self._get_iio_attr("voltage1", "quadrature_tracking_en", False, self._ctrl_c)

    @rx_quadrature_tracking_en_chan1_chip_c.setter
    def rx_quadrature_tracking_en_chan1_chip_c(self, value):
        self._set_iio_attr("voltage1", "quadrature_tracking_en", False, value, self._ctrl_c)

    @property
    def rx_quadrature_tracking_en_chan1_chip_d(self):
        """Enable Quadrature tracking calibration for RX2"""
        return self._get_iio_attr("voltage1", "quadrature_tracking_en", False, self._ctrl_d)

    @rx_quadrature_tracking_en_chan1_chip_d.setter
    def rx_quadrature_tracking_en_chan1_chip_d(self, value):
        self._set_iio_attr("voltage1", "quadrature_tracking_en", False, value, self._ctrl_d)

    @property
    def tx_quadrature_tracking_en_chan0_chip_c(self):
        """Enable Quadrature tracking calibration for TX1"""
        return self._get_iio_attr("voltage0", "quadrature_tracking_en", True, self._ctrl_c)

    @tx_quadrature_tracking_en_chan0_chip_c.setter
    def tx_quadrature_tracking_en_chan0_chip_c(self, value):
        self._set_iio_attr("voltage0", "quadrature_tracking_en", True, value, self._ctrl_c)

    @property
    def tx_quadrature_tracking_en_chan0_chip_d(self):
        """Enable Quadrature tracking calibration for TX1"""
        return self._get_iio_attr("voltage0", "quadrature_tracking_en", True, self._ctrl_d)

    @tx_quadrature_tracking_en_chan0_chip_d.setter
    def tx_quadrature_tracking_en_chan0_chip_d(self, value):
        self._set_iio_attr("voltage0", "quadrature_tracking_en", True, value, self._ctrl_d)

    @property
    def tx_quadrature_tracking_en_chan1_chip_c(self):
        """Enable Quadrature tracking calibration for TX2"""
        return self._get_iio_attr("voltage1", "quadrature_tracking_en", True, self._ctrl_c)

    @tx_quadrature_tracking_en_chan1_chip_c.setter
    def tx_quadrature_tracking_en_chan1_chip_c(self, value):
        self._set_iio_attr("voltage1", "quadrature_tracking_en", True, value, self._ctrl_c)

    @property
    def tx_quadrature_tracking_en_chan1_chip_d(self):
        """Enable Quadrature tracking calibration for TX2"""
        return self._get_iio_attr("voltage1", "quadrature_tracking_en", True, self._ctrl_d)

    @tx_quadrature_tracking_en_chan1_chip_d.setter
    def tx_quadrature_tracking_en_chan1_chip_d(self, value):
        self._set_iio_attr("voltage1", "quadrature_tracking_en", True, value, self._ctrl_d)

    @property
    def rx_powerdown_en_chan0_chip_c(self):
        """rx_powerdown_en_chan0: Enables/disables the RX1 signal paths
        while in the ENSM radio_on state"""
        return self._get_iio_attr("voltage0", "powerdown", False, self._ctrl_c)

    @rx_powerdown_en_chan0_chip_c.setter
    def rx_powerdown_en_chan0_chip_c(self, value):
        self._set_iio_attr("voltage0", "powerdown", False, value, self._ctrl_c)

    @property
    def rx_powerdown_en_chan0_chip_d(self):
        """rx_powerdown_en_chan0: Enables/disables the RX1 signal paths
        while in the ENSM radio_on state"""
        return self._get_iio_attr("voltage0", "powerdown", False, self._ctrl_d)

    @rx_powerdown_en_chan0_chip_d.setter
    def rx_powerdown_en_chan0_chip_d(self, value):
        self._set_iio_attr("voltage0", "powerdown", False, value, self._ctrl_d)

    @property
    def rx_powerdown_en_chan1_chip_c(self):
        """rx_powerdown_en_chan1: Enables/disables the RX2 signal paths
        while in the ENSM radio_on state"""
        return self._get_iio_attr("voltage1", "powerdown", False, self._ctrl_c)

    @rx_powerdown_en_chan1_chip_c.setter
    def rx_powerdown_en_chan1_chip_c(self, value):
        self._set_iio_attr("voltage1", "powerdown", False, value, self._ctrl_c)

    @property
    def rx_powerdown_en_chan1_chip_d(self):
        """rx_powerdown_en_chan1: Enables/disables the RX2 signal paths
        while in the ENSM radio_on state"""
        return self._get_iio_attr("voltage1", "powerdown", False, self._ctrl_d)

    @rx_powerdown_en_chan1_chip_d.setter
    def rx_powerdown_en_chan1_chip_d(self, value):
        self._set_iio_attr("voltage1", "powerdown", False, value, self._ctrl_d)

    @property
    def gain_control_mode_chan0_chip_c(self):
        """gain_control_mode_chan0_chip_c: Mode of receive path AGC. Options are:
        slow_attack, manual"""
        return self._get_iio_attr_str(
            "voltage0", "gain_control_mode", False, self._ctrl_c
        )

    @gain_control_mode_chan0_chip_c.setter
    def gain_control_mode_chan0_chip_c(self, value):
        self._set_iio_attr("voltage0", "gain_control_mode", False, value, self._ctrl_c)

    @property
    def gain_control_mode_chan0_chip_d(self):
        """gain_control_mode_chan0_chip_d: Mode of receive path AGC. Options are:
        slow_attack, manual"""
        return self._get_iio_attr_str(
            "voltage0", "gain_control_mode", False, self._ctrl_d
        )

    @gain_control_mode_chan0_chip_d.setter
    def gain_control_mode_chan0_chip_d(self, value):
        self._set_iio_attr("voltage0", "gain_control_mode", False, value, self._ctrl_d)

    @property
    def gain_control_mode_chan1_chip_c(self):
        """gain_control_mode_chan1_chip_c: Mode of receive path AGC. Options are:
        slow_attack, manual"""
        return self._get_iio_attr_str(
            "voltage1", "gain_control_mode", False, self._ctrl_c
        )

    @gain_control_mode_chan1_chip_c.setter
    def gain_control_mode_chan1_chip_c(self, value):
        self._set_iio_attr("voltage1", "gain_control_mode", False, value, self._ctrl_c)

    @property
    def gain_control_mode_chan1_chip_d(self):
        """gain_control_mode_chan1_chip_d: Mode of receive path AGC. Options are:
        slow_attack, manual"""
        return self._get_iio_attr_str(
            "voltage1", "gain_control_mode", False, self._ctrl_d
        )

    @gain_control_mode_chan1_chip_d.setter
    def gain_control_mode_chan1_chip_d(self, value):
        self._set_iio_attr("voltage1", "gain_control_mode", False, value, self._ctrl_d)

    @property
    def rx_hardwaregain_chan0_chip_c(self):
        """rx_hardwaregain: Gain applied to RX path channel 0. Only applicable when
        gain_control_mode is set to 'manual'"""
        return self._get_iio_attr("voltage0", "hardwaregain", False, self._ctrl_c)

    @rx_hardwaregain_chan0_chip_c.setter
    def rx_hardwaregain_chan0_chip_c(self, value):
        if self.gain_control_mode_chan0_chip_c == "manual":
            self._set_iio_attr("voltage0", "hardwaregain", False, value, self._ctrl_c)

    @property
    def rx_hardwaregain_chan0_chip_d(self):
        """rx_hardwaregain: Gain applied to RX path channel 0. Only applicable when
        gain_control_mode is set to 'manual'"""
        return self._get_iio_attr("voltage0", "hardwaregain", False, self._ctrl_d)

    @rx_hardwaregain_chan0_chip_d.setter
    def rx_hardwaregain_chan0_chip_d(self, value):
        if self.gain_control_mode_chan0_chip_d == "manual":
            self._set_iio_attr("voltage0", "hardwaregain", False, value, self._ctrl_d)

    @property
    def rx_hardwaregain_chan1_chip_c(self):
        """rx_hardwaregain: Gain applied to RX path channel 1. Only applicable when
        gain_control_mode is set to 'manual'"""
        return self._get_iio_attr("voltage1", "hardwaregain", False, self._ctrl_c)

    @rx_hardwaregain_chan1_chip_c.setter
    def rx_hardwaregain_chan1_chip_c(self, value):
        if self.gain_control_mode_chan1_chip_c == "manual":
            self._set_iio_attr("voltage1", "hardwaregain", False, value, self._ctrl_c)

    @property
    def rx_hardwaregain_chan1_chip_d(self):
        """rx_hardwaregain: Gain applied to RX path channel 1. Only applicable when
        gain_control_mode is set to 'manual'"""
        return self._get_iio_attr("voltage1", "hardwaregain", False, self._ctrl_d)

    @rx_hardwaregain_chan1_chip_d.setter
    def rx_hardwaregain_chan1_chip_d(self, value):
        if self.gain_control_mode_chan1_chip_d == "manual":
            self._set_iio_attr("voltage1", "hardwaregain", False, value, self._ctrl_d)

    @property
    def tx_hardwaregain_chan0_chip_c(self):
        """tx_hardwaregain: Attenuation applied to TX path channel 0"""
        return self._get_iio_attr("voltage0", "hardwaregain", True, self._ctrl_c)

    @tx_hardwaregain_chan0_chip_c.setter
    def tx_hardwaregain_chan0_chip_c(self, value):
        self._set_iio_attr("voltage0", "hardwaregain", True, value, self._ctrl_c)

    @property
    def tx_hardwaregain_chan0_chip_d(self):
        """tx_hardwaregain: Attenuation applied to TX path channel 0"""
        return self._get_iio_attr("voltage0", "hardwaregain", True, self._ctrl_d)

    @tx_hardwaregain_chan0_chip_d.setter
    def tx_hardwaregain_chan0_chip_d(self, value):
        self._set_iio_attr("voltage0", "hardwaregain", True, value, self._ctrl_d)

    @property
    def tx_hardwaregain_chan1_chip_c(self):
        """tx_hardwaregain: Attenuation applied to TX path channel 1"""
        return self._get_iio_attr("voltage1", "hardwaregain", True, self._ctrl_c)

    @tx_hardwaregain_chan1_chip_c.setter
    def tx_hardwaregain_chan1_chip_c(self, value):
        self._set_iio_attr("voltage1", "hardwaregain", True, value, self._ctrl_c)

    @property
    def tx_hardwaregain_chan1_chip_d(self):
        """tx_hardwaregain: Attenuation applied to TX path channel 1"""
        return self._get_iio_attr("voltage1", "hardwaregain", True, self._ctrl_d)

    @tx_hardwaregain_chan1_chip_d.setter
    def tx_hardwaregain_chan1_chip_d(self, value):
        self._set_iio_attr("voltage1", "hardwaregain", True, value, self._ctrl_d)

    @property
    def rx_rf_bandwidth_chip_c(self):
        """rx_rf_bandwidth: Bandwidth of front-end analog filter of RX path"""
        return self._get_iio_attr("voltage0", "rf_bandwidth", False, self._ctrl_c)

    @property
    def rx_rf_bandwidth_chip_d(self):
        """rx_rf_bandwidth: Bandwidth of front-end analog filter of RX path"""
        return self._get_iio_attr("voltage0", "rf_bandwidth", False, self._ctrl_d)

    @property
    def tx_rf_bandwidth_chip_c(self):
        """tx_rf_bandwidth: Bandwidth of front-end analog filter of TX path"""
        return self._get_iio_attr("voltage0", "rf_bandwidth", True, self._ctrl_c)

    @property
    def tx_rf_bandwidth_chip_d(self):
        """tx_rf_bandwidth: Bandwidth of front-end analog filter of TX path"""
        return self._get_iio_attr("voltage0", "rf_bandwidth", True, self._ctrl_d)

    @property
    def rx_sample_rate_chip_c(self):
        """rx_sample_rate: Sample rate RX path in samples per second"""
        return self._get_iio_attr("voltage0", "sampling_frequency", False, self._ctrl_c)

    @property
    def rx_sample_rate_chip_d(self):
        """rx_sample_rate: Sample rate RX path in samples per second"""
        return self._get_iio_attr("voltage0", "sampling_frequency", False, self._ctrl_d)

    @property
    def tx_sample_rate_chip_c(self):
        """tx_sample_rate: Sample rate TX path in samples per second"""
        return self._get_iio_attr("voltage0", "sampling_frequency", True, self._ctrl_c)

    @property
    def tx_sample_rate_chip_d(self):
        """tx_sample_rate: Sample rate TX path in samples per second"""
        return self._get_iio_attr("voltage0", "sampling_frequency", True, self._ctrl_d)

    @property
    def trx_lo_chip_c(self):
        """trx_lo: Carrier frequency of TX and RX path"""
        return self._get_iio_attr("altvoltage0", "frequency", True, self._ctrl_c)

    @trx_lo_chip_c.setter
    def trx_lo_chip_c(self, value):
        self._set_iio_attr("altvoltage0", "frequency", True, value, self._ctrl_c)

    @property
    def trx_lo_chip_d(self):
        """trx_lo: Carrier frequency of TX and RX path"""
        return self._get_iio_attr("altvoltage0", "frequency", True, self._ctrl_d)

    @trx_lo_chip_d.setter
    def trx_lo_chip_d(self, value):
        self._set_iio_attr("altvoltage0", "frequency", True, value, self._ctrl_d)
