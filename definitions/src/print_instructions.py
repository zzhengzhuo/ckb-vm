insts = [
    "VSETVLI",
    "VSETIVLI",
    "VSETVL",
    "VLM_V",
    "VLE8_V",
    "VLE16_V",
    "VLE32_V",
    "VLE64_V",
    "VLE128_V",
    "VLE256_V",
    "VLE512_V",
    "VLE1024_V",
    "VSM_V",
    "VSE8_V",
    "VSE16_V",
    "VSE32_V",
    "VSE64_V",
    "VSE128_V",
    "VSE256_V",
    "VSE512_V",
    "VSE1024_V",
    "VADD_VV",
    "VADD_VX",
    "VADD_VI",
    "VSUB_VV",
    "VSUB_VX",
    "VRSUB_VX",
    "VRSUB_VI",
    "VMUL_VV",
    "VMUL_VX",
    "VDIV_VV",
    "VDIV_VX",
    "VDIVU_VV",
    "VDIVU_VX",
    "VREM_VV",
    "VREM_VX",
    "VREMU_VV",
    "VREMU_VX",
    "VSLL_VV",
    "VSLL_VX",
    "VSLL_VI",
    "VSRL_VV",
    "VSRL_VX",
    "VSRL_VI",
    "VSRA_VV",
    "VSRA_VX",
    "VSRA_VI",
    "VMSEQ_VV",
    "VMSEQ_VX",
    "VMSEQ_VI",
    "VMSNE_VV",
    "VMSNE_VX",
    "VMSNE_VI",
    "VMSLTU_VV",
    "VMSLTU_VX",
    "VMSLT_VV",
    "VMSLT_VX",
    "VMSLEU_VV",
    "VMSLEU_VX",
    "VMSLEU_VI",
    "VMSLE_VV",
    "VMSLE_VX",
    "VMSLE_VI",
    "VMSGTU_VX",
    "VMSGTU_VI",
    "VMSGT_VX",
    "VMSGT_VI",
    "VMINU_VV",
    "VMINU_VX",
    "VMIN_VV",
    "VMIN_VX",
    "VMAXU_VV",
    "VMAXU_VX",
    "VMAX_VV",
    "VMAX_VX",
    "VWADDU_VV",
    "VWADDU_VX",
    "VWSUBU_VV",
    "VWSUBU_VX",
    "VWADD_VV",
    "VWADD_VX",
    "VWSUB_VV",
    "VWSUB_VX",
    "VWADDU_WV",
    "VWADDU_WX",
    "VWSUBU_WV",
    "VWSUBU_WX",
    "VWADD_WV",
    "VWADD_WX",
    "VWSUB_WV",
    "VWSUB_WX",
    "VZEXT_VF8",
    "VSEXT_VF8",
    "VZEXT_VF4",
    "VSEXT_VF4",
    "VZEXT_VF2",
    "VSEXT_VF2",
    "VADC_VVM",
    "VADC_VXM",
    "VADC_VIM",
    "VMADC_VVM",
    "VMADC_VXM",
    "VMADC_VIM",
    "VMADC_VV",
    "VMADC_VX",
    "VMADC_VI",
    "VSBC_VVM",
    "VSBC_VXM",
    "VMSBC_VVM",
    "VMSBC_VXM",
    "VMSBC_VV",
    "VMSBC_VX",
    "VAND_VV",
    "VAND_VI",
    "VAND_VX",
    "VOR_VV",
    "VOR_VX",
    "VOR_VI",
    "VXOR_VV",
    "VXOR_VX",
    "VXOR_VI",
    "VNSRL_WV",
    "VNSRL_WX",
    "VNSRL_WI",
    "VNSRA_WV",
    "VNSRA_WX",
    "VNSRA_WI",
    "VMULH_VV",
    "VMULH_VX",
    "VMULHU_VV",
    "VMULHU_VX",
    "VMULHSU_VV",
    "VMULHSU_VX",
    "VWMULU_VV",
    "VWMULU_VX",
    "VWMULSU_VV",
    "VWMULSU_VX",
    "VWMUL_VV",
    "VWMUL_VX",
    "VMV_V_V",
    "VMV_V_X",
    "VMV_V_I",
    "VSADDU_VV",
    "VSADDU_VX",
    "VSADDU_VI",
    "VSADD_VV",
    "VSADD_VX",
    "VSADD_VI",
    "VSSUBU_VV",
    "VSSUBU_VX",
    "VSSUB_VV",
    "VSSUB_VX",
    "VAADDU_VV",
    "VAADDU_VX",
    "VAADD_VV",
    "VAADD_VX",
    "VASUBU_VV",
    "VASUBU_VX",
    "VASUB_VV",
    "VASUB_VX",
    "VMV1R_V",
    "VMV2R_V",
    "VMV4R_V",
    "VMV8R_V",
    "VFIRST_M",
    "VMAND_MM",
    "VMNAND_MM",
    "VMANDNOT_MM",
    "VMXOR_MM",
    "VMOR_MM",
    "VMNOR_MM",
    "VMORNOT_MM",
    "VMXNOR_MM",
    "VLSE8_V",
    "VLSE16_V",
    "VLSE32_V",
    "VLSE64_V",
    "VLSE128_V",
    "VLSE256_V",
    "VLSE512_V",
    "VLSE1024_V",
    "VSSE8_V",
    "VSSE16_V",
    "VSSE32_V",
    "VSSE64_V",
    "VSSE128_V",
    "VSSE256_V",
    "VSSE512_V",
    "VSSE1024_V",
    "VLUXEI8_V",
    "VLUXEI16_V",
    "VLUXEI32_V",
    "VLUXEI64_V",
    "VLUXEI128_V",
    "VLUXEI256_V",
    "VLUXEI512_V",
    "VLUXEI1024_V",
    "VLOXEI8_V",
    "VLOXEI16_V",
    "VLOXEI32_V",
    "VLOXEI64_V",
    "VLOXEI128_V",
    "VLOXEI256_V",
    "VLOXEI512_V",
    "VLOXEI1024_V",
    "VSUXEI8_V",
    "VSUXEI16_V",
    "VSUXEI32_V",
    "VSUXEI64_V",
    "VSUXEI128_V",
    "VSUXEI256_V",
    "VSUXEI512_V",
    "VSUXEI1024_V",
    "VSOXEI8_V",
    "VSOXEI16_V",
    "VSOXEI32_V",
    "VSOXEI64_V",
    "VSOXEI128_V",
    "VSOXEI256_V",
    "VSOXEI512_V",
    "VSOXEI1024_V",
    "VL1RE8_V",
    "VL1RE16_V",
    "VL1RE32_V",
    "VL1RE64_V",
    "VL2RE8_V",
    "VL2RE16_V",
    "VL2RE32_V",
    "VL2RE64_V",
    "VL4RE8_V",
    "VL4RE16_V",
    "VL4RE32_V",
    "VL4RE64_V",
    "VL8RE8_V",
    "VL8RE16_V",
    "VL8RE32_V",
    "VL8RE64_V",
    "VS1R_V",
    "VS2R_V",
    "VS4R_V",
    "VS8R_V",
    "VMACC_VV",
    "VMACC_VX",
    "VNMSAC_VV",
    "VNMSAC_VX",
    "VMADD_VV",
    "VMADD_VX",
    "VNMSUB_VV",
    "VNMSUB_VX",
    "VSSRL_VV",
    "VSSRL_VX",
    "VSSRL_VI",
    "VSSRA_VV",
    "VSSRA_VX",
    "VSSRA_VI",
    "VSMUL_VV",
    "VSMUL_VX",
    "VWMACCU_VV",
    "VWMACCU_VX",
    "VWMACC_VV",
    "VWMACC_VX",
    "VWMACCSU_VV",
    "VWMACCSU_VX",
    "VWMACCUS_VX",
    "VMERGE_VVM",
    "VMERGE_VXM",
    "VMERGE_VIM",
    "VNCLIPU_WV",
    "VNCLIPU_WX",
    "VNCLIPU_WI",
    "VNCLIP_WV",
    "VNCLIP_WX",
    "VNCLIP_WI",
    "VREDSUM_VS",
    "VREDAND_VS",
    "VREDOR_VS",
    "VREDXOR_VS",
    "VREDMINU_VS",
    "VREDMIN_VS",
    "VREDMAXU_VS",
    "VREDMAX_VS",
    "VWREDSUMU_VS",
    "VWREDSUM_VS",
    "VCPOP",
    "VMSBF_M",
    "VMSOF_M",
    "VMSIF_M",
    "VIOTA_M",
    "VID_V",
    "VMV_X_S",
    "VMV_S_X",
    "VCOMPRESS_VM",
    "VSLIDE1UP_VX",
    "VSLIDEUP_VX",
    "VSLIDEUP_VI",
    "VSLIDE1DOWN_VX",
    "VSLIDEDOWN_VX",
    "VSLIDEDOWN_VI",
    "VRGATHER_VX",
    "VRGATHER_VV",
    "VRGATHEREI16_VV",
    "VRGATHER_VI",
]

for (i, e) in enumerate(insts):
    if i >= 256:
        i = i - 256
        print(f'pub const OP_{e}: InstructionOpcode = 0x{i:02x}f1;')
    else:
        print(f'pub const OP_{e}: InstructionOpcode = 0x{i:02x}f0;')
