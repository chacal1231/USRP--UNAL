#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: OFDM Tx
# Description: Example of an OFDM Transmitter
# Generated: Fri Nov 18 03:28:20 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.digital.utils import tagged_streams
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import math
import numpy
import random
import sip
import sys
import threading
import time


class OFDM_Tx_Rx_time(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "OFDM Tx")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("OFDM Tx")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "OFDM_Tx_Rx_time")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 1
        self.pilot_symbols = pilot_symbols = ((1, 1, 1,1, -1,1, 1, 1,1, -1),)
        self.pilot_carriers = pilot_carriers = ((-49,-35,-27,-21, -7, 7, 21,27,35,49),)
        self.payload_mod = payload_mod = digital.constellation_qpsk()
        self.occupied_carriers = occupied_carriers = (range(-50,-49)+range(-48,-35)+range(-34,-27)+range(-26, -21) + range(-20, -7) + range(-6, 0) + range(1, 7) + range(8, 21) + range(22, 27)+range(28,35)+range(36,49)+range(50,51),)
        self.length_tag_key_rx = length_tag_key_rx = "frame_len"
        self.length_tag_key = length_tag_key = "packet_len"
        self.header_mod = header_mod = digital.constellation_bpsk()
        self.fft_len = fft_len = 128
        self.eb = eb = 0.35
        self.sync_word2 = sync_word2 = [0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1,0, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 0, 0, 0, 0, 0,0, 0, 0, 0, 0] 
        self.sync_word1 = sync_word1 = [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]
        self.samp_rate = samp_rate = int(2e6)
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(32, 32, 1.0/float(sps), eb, 45*32)
        self.rolloff = rolloff = 0
        self.probe_var = probe_var = 0
        self.payload_equalizer = payload_equalizer = digital.ofdm_equalizer_simpledfe(fft_len, payload_mod.base(), occupied_carriers, pilot_carriers, pilot_symbols, 1)
        self.packet_len = packet_len = 96
        self.header_formatter_rx = header_formatter_rx = digital.packet_header_ofdm(occupied_carriers, n_syms=1, len_tag_key=length_tag_key, frame_len_tag_key=length_tag_key_rx, bits_per_header_sym=header_mod.bits_per_symbol(), bits_per_payload_sym=payload_mod.bits_per_symbol(), scramble_header=False)
        self.header_formatter = header_formatter = digital.packet_header_ofdm(occupied_carriers, 1, length_tag_key)
        self.header_equalizer = header_equalizer = digital.ofdm_equalizer_simpledfe(fft_len, header_mod.base(), occupied_carriers, pilot_carriers, pilot_symbols)
        self.bpsym = bpsym = 2
        self.EbN0 = EbN0 = 2

        ##################################################
        # Blocks
        ##################################################
        self.probe_signal = analog.probe_avg_mag_sqrd_c(0, 1)
        self.qtgui_time_sink_x_3 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_3.set_update_time(0.10)
        self.qtgui_time_sink_x_3.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_3.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_3.enable_tags(-1, True)
        self.qtgui_time_sink_x_3.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_3.enable_autoscale(False)
        self.qtgui_time_sink_x_3.enable_grid(False)
        self.qtgui_time_sink_x_3.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_3.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_3.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_3.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_3.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_3.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_3.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_3.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_3.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_3.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_3_win = sip.wrapinstance(self.qtgui_time_sink_x_3.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_3_win)
        self.qtgui_number_sink_1 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_1.set_update_time(0.10)
        self.qtgui_number_sink_1.set_title("")
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                 "", "", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_1.set_min(i, -1)
            self.qtgui_number_sink_1.set_max(i, 1)
            self.qtgui_number_sink_1.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_1.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_1.set_label(i, labels[i])
            self.qtgui_number_sink_1.set_unit(i, units[i])
            self.qtgui_number_sink_1.set_factor(i, factor[i])
        
        self.qtgui_number_sink_1.enable_autoscale(False)
        self._qtgui_number_sink_1_win = sip.wrapinstance(self.qtgui_number_sink_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_1_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            1,
            qtgui.NUM_GRAPH_NONE,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("")
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                 "", "", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, -1)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0.enable_autoscale(True)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"enviado", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_1.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1.set_plot_pos_half(not True)
        
        labels = ["USRP Tx+N", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_1_win)
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
        	256, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(False)
        
        if not True:
          self.qtgui_const_sink_x_0_0.disable_legend()
        
        labels = ["QPSK_mod", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_0_win)
        def _probe_var_probe():
            while True:
                val = self.probe_signal.level()
                try:
                    self.set_probe_var(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (100))
        _probe_var_thread = threading.Thread(target=_probe_var_probe)
        _probe_var_thread.daemon = True
        _probe_var_thread.start()
        self.fft_vxx_1 = fft.fft_vcc(fft_len, True, (), True, 1)
        self.fft_vxx_0_0 = fft.fft_vcc(fft_len, True, (()), True, 1)
        self.fft_vxx_0 = fft.fft_vcc(fft_len, False, (()), True, 1)
        self.digital_pfb_clock_sync_xxx_0_0 = digital.pfb_clock_sync_ccf(sps, 6.28/100.0, (rrc_taps), 32, 16, 1.5, 1)
        self.digital_packet_headerparser_b_0 = digital.packet_headerparser_b(header_formatter_rx.base())
        self.digital_packet_headergenerator_bb_0 = digital.packet_headergenerator_bb(header_formatter.formatter(), length_tag_key)
        self.digital_ofdm_sync_sc_cfb_0 = digital.ofdm_sync_sc_cfb(fft_len, fft_len/4, False)
        self.digital_ofdm_serializer_vcc_payload = digital.ofdm_serializer_vcc(fft_len, occupied_carriers, length_tag_key_rx, length_tag_key, 1, "", True)
        self.digital_ofdm_serializer_vcc_header = digital.ofdm_serializer_vcc(fft_len, occupied_carriers, length_tag_key_rx, "", 0, "", True)
        self.digital_ofdm_frame_equalizer_vcvc_1 = digital.ofdm_frame_equalizer_vcvc(payload_equalizer.base(), fft_len/4, length_tag_key_rx, True, 0)
        self.digital_ofdm_frame_equalizer_vcvc_0 = digital.ofdm_frame_equalizer_vcvc(header_equalizer.base(), fft_len/4, length_tag_key_rx, True, 1)
        self.digital_ofdm_cyclic_prefixer_0 = digital.ofdm_cyclic_prefixer(fft_len, fft_len+fft_len/4, rolloff, length_tag_key)
        self.digital_ofdm_chanest_vcvc_0 = digital.ofdm_chanest_vcvc((sync_word1), (sync_word2), 1, 0, 3, False)
        self.digital_ofdm_carrier_allocator_cvc_0 = digital.ofdm_carrier_allocator_cvc(fft_len, occupied_carriers, pilot_carriers, pilot_symbols, (sync_word1, sync_word2), length_tag_key)
        self.digital_header_payload_demux_0 = digital.header_payload_demux(
        	  3,
        	  fft_len,
        	  fft_len/4,
        	  length_tag_key_rx,
        	  "",
        	  True,
        	  gr.sizeof_gr_complex,
        	  "rx_time",
                  samp_rate,
                  (),
            )
        self.digital_constellation_decoder_cb_1 = digital.constellation_decoder_cb(payload_mod.base())
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(header_mod.base())
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_bc((payload_mod.points()), 1)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((header_mod.points()), 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_gr_complex*1, length_tag_key, 0)
        self.blocks_tag_gate_0 = blocks.tag_gate(gr.sizeof_gr_complex * 1, False)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, packet_len, length_tag_key)
        self.blocks_rms_xx_1 = blocks.rms_cf(0.0001)
        self.blocks_rms_xx_0 = blocks.rms_cf(0.0001)
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(payload_mod.bits_per_symbol(), 8, length_tag_key, True, gr.GR_LSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(8, bpsym, length_tag_key, False, gr.GR_LSB_FIRST)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((0.05, ))
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_char*1, "/home/juandavid/rx_experimental_18 Nov/Antenas Banda ancha/rx_files_Antena_18 Nov/rx_0.00.txt", False)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, "/home/juandavid/rx_experimental_18 Nov/Antenas Banda ancha/rx_files_Antena_18 Nov/rx_0.00.txt", False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, "/home/juandavid/rx.txt", False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, fft_len+fft_len/4)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blks2_error_rate_0 = grc_blks2.error_rate(
        	type='BER',

        	win_size=int(4e6),
        	bits_per_symbol=payload_mod.bits_per_symbol(),
        )
        self.analog_noise_source_x = analog.noise_source_c(analog.GR_GAUSSIAN, 0.00, 42)
        self.analog_frequency_modulator_fc_0 = analog.frequency_modulator_fc(-2.0/fft_len)
        self._EbN0_range = Range(-20, 200, 1, 2, 200)
        self._EbN0_win = RangeWidget(self._EbN0_range, self.set_EbN0, "Eb / N0 (dB)", "counter_slider", float)
        self.top_layout.addWidget(self._EbN0_win)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.digital_packet_headerparser_b_0, 'header_data'), (self.digital_header_payload_demux_0, 'header_data'))    
        self.connect((self.analog_frequency_modulator_fc_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.analog_noise_source_x, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.analog_noise_source_x, 0), (self.qtgui_time_sink_x_3, 0))    
        self.connect((self.blks2_error_rate_0, 0), (self.qtgui_number_sink_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_freq_sink_x_1, 0))    
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.blocks_file_source_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))    
        self.connect((self.blocks_file_source_0_0, 0), (self.blks2_error_rate_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_rms_xx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_rms_xx_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_tag_gate_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.digital_header_payload_demux_0, 0))    
        self.connect((self.blocks_multiply_xx_1, 0), (self.qtgui_number_sink_1, 0))    
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))    
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.blks2_error_rate_0, 0))    
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.blocks_rms_xx_0, 0), (self.blocks_multiply_xx_1, 0))    
        self.connect((self.blocks_rms_xx_1, 0), (self.blocks_multiply_xx_1, 1))    
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_repack_bits_bb_0, 0))    
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.digital_packet_headergenerator_bb_0, 0))    
        self.connect((self.blocks_tag_gate_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.digital_ofdm_carrier_allocator_cvc_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_delay_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.digital_ofdm_sync_sc_cfb_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.probe_signal, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_tagged_stream_mux_0, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.blocks_tagged_stream_mux_0, 1))    
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.digital_packet_headerparser_b_0, 0))    
        self.connect((self.digital_constellation_decoder_cb_1, 0), (self.blocks_repack_bits_bb_0_0, 0))    
        self.connect((self.digital_header_payload_demux_0, 0), (self.fft_vxx_0_0, 0))    
        self.connect((self.digital_header_payload_demux_0, 1), (self.fft_vxx_1, 0))    
        self.connect((self.digital_ofdm_carrier_allocator_cvc_0, 0), (self.fft_vxx_0, 0))    
        self.connect((self.digital_ofdm_chanest_vcvc_0, 0), (self.digital_ofdm_frame_equalizer_vcvc_0, 0))    
        self.connect((self.digital_ofdm_cyclic_prefixer_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.digital_ofdm_frame_equalizer_vcvc_0, 0), (self.digital_ofdm_serializer_vcc_header, 0))    
        self.connect((self.digital_ofdm_frame_equalizer_vcvc_1, 0), (self.digital_ofdm_serializer_vcc_payload, 0))    
        self.connect((self.digital_ofdm_serializer_vcc_header, 0), (self.digital_constellation_decoder_cb_0, 0))    
        self.connect((self.digital_ofdm_serializer_vcc_payload, 0), (self.digital_constellation_decoder_cb_1, 0))    
        self.connect((self.digital_ofdm_serializer_vcc_payload, 0), (self.digital_pfb_clock_sync_xxx_0_0, 0))    
        self.connect((self.digital_ofdm_sync_sc_cfb_0, 0), (self.analog_frequency_modulator_fc_0, 0))    
        self.connect((self.digital_ofdm_sync_sc_cfb_0, 1), (self.digital_header_payload_demux_0, 1))    
        self.connect((self.digital_packet_headergenerator_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0_0, 0), (self.qtgui_const_sink_x_0_0, 0))    
        self.connect((self.fft_vxx_0, 0), (self.digital_ofdm_cyclic_prefixer_0, 0))    
        self.connect((self.fft_vxx_0_0, 0), (self.digital_ofdm_chanest_vcvc_0, 0))    
        self.connect((self.fft_vxx_1, 0), (self.digital_ofdm_frame_equalizer_vcvc_1, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "OFDM_Tx_Rx_time")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(32, 32, 1.0/float(self.sps), self.eb, 45*32))

    def get_pilot_symbols(self):
        return self.pilot_symbols

    def set_pilot_symbols(self, pilot_symbols):
        self.pilot_symbols = pilot_symbols
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.header_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols))
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 1))

    def get_pilot_carriers(self):
        return self.pilot_carriers

    def set_pilot_carriers(self, pilot_carriers):
        self.pilot_carriers = pilot_carriers
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.header_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols))
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 1))

    def get_payload_mod(self):
        return self.payload_mod

    def set_payload_mod(self, payload_mod):
        self.payload_mod = payload_mod
        self.set_header_formatter_rx(digital.packet_header_ofdm(self.occupied_carriers, n_syms=1, len_tag_key=self.length_tag_key, frame_len_tag_key=self.length_tag_key_rx, bits_per_header_sym=self.header_mod.bits_per_symbol(), bits_per_payload_sym=self.payload_mod.bits_per_symbol(), scramble_header=False))
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 1))
        self.blocks_repack_bits_bb_0_0.set_k_and_l(self.payload_mod.bits_per_symbol(),8)
        self.digital_chunks_to_symbols_xx_0_0.set_symbol_table((self.payload_mod.points()))

    def get_occupied_carriers(self):
        return self.occupied_carriers

    def set_occupied_carriers(self, occupied_carriers):
        self.occupied_carriers = occupied_carriers
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.header_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols))
        self.set_header_formatter(digital.packet_header_ofdm(self.occupied_carriers, 1, self.length_tag_key))
        self.set_header_formatter_rx(digital.packet_header_ofdm(self.occupied_carriers, n_syms=1, len_tag_key=self.length_tag_key, frame_len_tag_key=self.length_tag_key_rx, bits_per_header_sym=self.header_mod.bits_per_symbol(), bits_per_payload_sym=self.payload_mod.bits_per_symbol(), scramble_header=False))
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 1))

    def get_length_tag_key_rx(self):
        return self.length_tag_key_rx

    def set_length_tag_key_rx(self, length_tag_key_rx):
        self.length_tag_key_rx = length_tag_key_rx
        self.set_header_formatter_rx(digital.packet_header_ofdm(self.occupied_carriers, n_syms=1, len_tag_key=self.length_tag_key, frame_len_tag_key=self.length_tag_key_rx, bits_per_header_sym=self.header_mod.bits_per_symbol(), bits_per_payload_sym=self.payload_mod.bits_per_symbol(), scramble_header=False))

    def get_length_tag_key(self):
        return self.length_tag_key

    def set_length_tag_key(self, length_tag_key):
        self.length_tag_key = length_tag_key
        self.set_header_formatter(digital.packet_header_ofdm(self.occupied_carriers, 1, self.length_tag_key))
        self.set_header_formatter_rx(digital.packet_header_ofdm(self.occupied_carriers, n_syms=1, len_tag_key=self.length_tag_key, frame_len_tag_key=self.length_tag_key_rx, bits_per_header_sym=self.header_mod.bits_per_symbol(), bits_per_payload_sym=self.payload_mod.bits_per_symbol(), scramble_header=False))

    def get_header_mod(self):
        return self.header_mod

    def set_header_mod(self, header_mod):
        self.header_mod = header_mod
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.header_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols))
        self.set_header_formatter_rx(digital.packet_header_ofdm(self.occupied_carriers, n_syms=1, len_tag_key=self.length_tag_key, frame_len_tag_key=self.length_tag_key_rx, bits_per_header_sym=self.header_mod.bits_per_symbol(), bits_per_payload_sym=self.payload_mod.bits_per_symbol(), scramble_header=False))
        self.digital_chunks_to_symbols_xx_0.set_symbol_table((self.header_mod.points()))

    def get_fft_len(self):
        return self.fft_len

    def set_fft_len(self, fft_len):
        self.fft_len = fft_len
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.header_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols))
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 1))
        self.analog_frequency_modulator_fc_0.set_sensitivity(-2.0/self.fft_len)
        self.blocks_delay_0.set_dly(self.fft_len+self.fft_len/4)

    def get_eb(self):
        return self.eb

    def set_eb(self, eb):
        self.eb = eb
        self.set_rrc_taps(firdes.root_raised_cosine(32, 32, 1.0/float(self.sps), self.eb, 45*32))

    def get_sync_word2(self):
        return self.sync_word2

    def set_sync_word2(self, sync_word2):
        self.sync_word2 = sync_word2

    def get_sync_word1(self):
        return self.sync_word1

    def set_sync_word1(self, sync_word1):
        self.sync_word1 = sync_word1

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_3.set_samp_rate(self.samp_rate)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.digital_pfb_clock_sync_xxx_0_0.update_taps((self.rrc_taps))

    def get_rolloff(self):
        return self.rolloff

    def set_rolloff(self, rolloff):
        self.rolloff = rolloff

    def get_probe_var(self):
        return self.probe_var

    def set_probe_var(self, probe_var):
        self.probe_var = probe_var

    def get_payload_equalizer(self):
        return self.payload_equalizer

    def set_payload_equalizer(self, payload_equalizer):
        self.payload_equalizer = payload_equalizer

    def get_packet_len(self):
        return self.packet_len

    def set_packet_len(self, packet_len):
        self.packet_len = packet_len
        self.blocks_stream_to_tagged_stream_0.set_packet_len(self.packet_len)
        self.blocks_stream_to_tagged_stream_0.set_packet_len_pmt(self.packet_len)

    def get_header_formatter_rx(self):
        return self.header_formatter_rx

    def set_header_formatter_rx(self, header_formatter_rx):
        self.header_formatter_rx = header_formatter_rx

    def get_header_formatter(self):
        return self.header_formatter

    def set_header_formatter(self, header_formatter):
        self.header_formatter = header_formatter
        self.digital_packet_headergenerator_bb_0.set_header_formatter(self.header_formatter.formatter())

    def get_header_equalizer(self):
        return self.header_equalizer

    def set_header_equalizer(self, header_equalizer):
        self.header_equalizer = header_equalizer

    def get_bpsym(self):
        return self.bpsym

    def set_bpsym(self, bpsym):
        self.bpsym = bpsym
        self.blocks_repack_bits_bb_0.set_k_and_l(8,self.bpsym)

    def get_EbN0(self):
        return self.EbN0

    def set_EbN0(self, EbN0):
        self.EbN0 = EbN0


def main(top_block_cls=OFDM_Tx_Rx_time, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable real-time scheduling."

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    ii=0
    tb = top_block_cls()
    tb.start()
    #t0 = time.clock() #or time.clock()
    tb.show()
    #http://stackoverflow.com/questions/38099471/interrupting-a-simple-gnuradio-flow

    while True:
	n=tb.probe_var
	print n,
	if (n>3e-9 and ii==0):
	 ii=1
         t0 = time.clock() 
	 break
	else:
	 if ((n<=1e-9 ) and ii>=1):
	  ii+=1
	  print "resultadotiempo",
	  print ii,
	  if ii==100:
	  	 print time.clock()-t0, 
	         tb.stop()	
	  	 break 

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()