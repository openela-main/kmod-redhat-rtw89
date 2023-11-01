%define kmod_name		rtw89
%define kmod_vendor		redhat
%define kmod_rpm_name		kmod-redhat-rtw89
%define kmod_driver_version	5.14.0_284.11.1_dup9.2
%define kmod_driver_epoch	%{nil}
%define kmod_rpm_release	1
%define kmod_kernel_version	5.14.0-284.11.1.el9_2
%define kmod_kernel_version_min	5.14.0-284
%define kmod_kernel_version_dep	5.14.0-284.el9
%define kmod_kbuild_dir		drivers/net/wireless/realtek/rtw89
%define kmod_dependencies       %{nil}
%define kmod_dist_build_deps	%{nil}
%define kmod_build_dependencies	%{nil}
%define kmod_provides           %{nil}
%define kmod_devel_package	1
%define kmod_devel_src_paths	%{nil}
%define kmod_install_path	extra/kmod-redhat-rtw89
%define kmod_files_package	0
%define kmod_files_noarch	1
%define kernel_pkg		kernel
%define kernel_devel_pkg	kernel-devel
%define kernel_modules_pkg	kernel-modules

%{!?dist: %define dist .el9_2}
%{!?make_build: %define make_build make}

%if "%{kmod_kernel_version_dep}" == ""
%define kmod_kernel_version_dep %{kmod_kernel_version}
%endif

%if "%{kmod_dist_build_deps}" == ""
%if (0%{?rhel} > 8) || (0%{?centos} > 8)
%define abi_list stablelist
%define kmod_dist_build_deps redhat-rpm-config kernel-abi-stablelists elfutils-libelf-devel kernel-rpm-macros kmod
%else
%if (0%{?rhel} > 7) || (0%{?centos} > 7)
%define abi_list whitelist
%define kmod_dist_build_deps redhat-rpm-config kernel-abi-whitelists elfutils-libelf-devel kernel-rpm-macros kmod
%else
%define abi_list whitelist
%define kmod_dist_build_deps redhat-rpm-config kernel-abi-whitelists
%endif
%endif
%endif

Source0:	%{kmod_name}-%{kmod_vendor}-%{kmod_driver_version}.tar.bz2
# Source code patches
Patch0:	0001-wifi-rtw89-8852b-add-BB-and-RF-tables-1-of-2.patch
Patch1:	0002-wifi-rtw89-8852b-add-BB-and-RF-tables-2-of-2.patch
Patch2:	0003-wifi-rtw89-8852b-add-tables-for-RFK.patch
Patch3:	0004-wifi-rtw89-phy-make-generic-txpwr-setting-functions.patch
Patch4:	0005-wifi-rtw89-debug-txpwr_table-considers-sign.patch
Patch5:	0006-wifi-rtw89-8852b-add-chip_ops-set_txpwr.patch
Patch6:	0007-wifi-rtw89-8852b-add-chip_ops-to-read-efuse.patch
Patch7:	0008-wifi-rtw89-8852b-add-chip_ops-to-read-phy-cap.patch
Patch8:	0009-wifi-rtw89-8852be-add-8852BE-PCI-entry.patch
Patch9:	0010-wifi-rtw89-8852c-correct-set-of-IQK-backup-registers.patch
Patch10:	0011-wifi-rtw89-8852c-rfk-correct-miscoding-delay-of-DPK.patch
Patch11:	0012-wifi-rtw89-8852c-update-BB-parameters-to-v28.patch
Patch12:	0013-wifi-rtw89-phy-ignore-warning-of-bb-gain-cfg_type-4.patch
Patch13:	0014-wifi-rtw89-8852c-set-pin-MUX-to-enable-BT-firmware-l.patch
Patch14:	0015-wifi-rtw89-add-to-dump-TX-FIFO-0-1-for-8852C.patch
Patch15:	0016-wifi-rtw89-coex-move-chip_ops-btc_bt_aci_imp-to-a-ge.patch
Patch16:	0017-wifi-rtw89-parse-PHY-status-only-when-PPDU-is-to_sel.patch
Patch17:	0018-wifi-rtw89-8852b-set-proper-configuration-before-loa.patch
Patch18:	0019-wifi-rtw89-8852b-add-HFC-quota-arrays.patch
Patch19:	0020-wifi-rtw89-make-generic-functions-to-convert-subband.patch
Patch20:	0021-wifi-rtw89-8852b-add-chip_ops-set_channel.patch
Patch21:	0022-wifi-rtw89-correct-6-GHz-scan-behavior.patch
Patch22:	0023-wifi-rtw89-fix-wrong-bandwidth-settings-after-scan.patch
Patch23:	0024-wifi-rtw89-8852b-add-chip_ops-set_channel_help.patch
Patch24:	0025-wifi-rtw89-8852b-add-power-on-off-functions.patch
Patch25:	0026-wifi-rtw89-8852b-add-basic-baseband-chip_ops.patch
Patch26:	0027-wifi-rtw89-8852b-add-chip_ops-to-get-thermal.patch
Patch27:	0028-wifi-rtw89-8852b-add-chip_ops-related-to-BT-coexiste.patch
Patch28:	0029-wifi-rtw89-8852b-add-chip_ops-to-query-PPDU.patch
Patch29:	0030-wifi-rtw89-8852b-add-chip_ops-to-configure-TX-RX-pat.patch
Patch30:	0031-wifi-rtw89-8852b-add-functions-to-control-BB-to-assi.patch
Patch31:	0032-wifi-rtw89-8852b-add-basic-attributes-of-chip_info.patch
Patch32:	0033-wifi-rtw89-8852b-rfk-add-DACK.patch
Patch33:	0034-wifi-rtw89-8852b-rfk-add-RCK.patch
Patch34:	0035-wifi-rtw89-8852b-rfk-add-RX-DCK.patch
Patch35:	0036-wifi-rtw89-8852b-rfk-add-IQK.patch
Patch36:	0037-wifi-rtw89-8852b-rfk-add-TSSI.patch
Patch37:	0038-wifi-rtw89-8852b-rfk-add-DPK.patch
Patch38:	0039-wifi-rtw89-8852b-add-chip_ops-related-to-RF-calibrat.patch
Patch39:	0040-wifi-rtw89-phy-add-dummy-C2H-handler-to-avoid-warnin.patch
Patch40:	0041-wifi-rtw89-8852b-add-8852be-to-Makefile-and-Kconfig.patch
Patch41:	0042-wifi-rtw89-fw-adapt-to-new-firmware-format-of-dynami.patch
Patch42:	0043-wifi-rtw89-declare-support-bands-with-const.patch
Patch43:	0044-wifi-rtw89-8852c-make-table-of-RU-mask-constant.patch
Patch44:	0045-wifi-rtw89-add-BW-info-for-both-TX-and-RX-in-phy_inf.patch
Patch45:	0046-wifi-rtw89-check-if-sta-s-mac_id-is-valid-under-AP-T.patch
Patch46:	0047-wifi-rtw89-collect-and-send-RF-parameters-to-firmwar.patch
Patch47:	0048-wifi-rtw89-move-enable_cpu-disable_cpu-into-fw_downl.patch
Patch48:	0049-wifi-rtw89-add-function-to-adjust-and-restore-PLE-qu.patch
Patch49:	0050-wifi-rtw89-add-drop-tx-packet-function.patch
Patch50:	0051-wifi-rtw89-add-related-H2C-for-WoWLAN-mode.patch
Patch51:	0052-wifi-rtw89-add-WoWLAN-function-support.patch
Patch52:	0053-wifi-rtw89-add-WoWLAN-pattern-match-support.patch
Patch53:	0054-wifi-rtw89-8852b-Fix-spelling-mistake-KIP_RESOTRE-KI.patch
Patch54:	0055-wifi-rtw89-dump-dispatch-status-via-debug-port.patch
Patch55:	0056-wifi-rtw89-update-D-MAC-and-C-MAC-dump-to-diagnose-S.patch
Patch56:	0057-wifi-rtw89-8852b-change-debug-mask-of-message-of-no-.patch
Patch57:	0058-wifi-rtw89-Fix-some-error-handling-path-in-rtw89_wow.patch
Patch58:	0059-wifi-rtw89-8852b-correct-TX-power-controlled-by-BT-c.patch
Patch59:	0060-wifi-rtw89-read-CFO-from-FD-or-preamble-CFO-field-of.patch
Patch60:	0061-wifi-rtw89-switch-BANDEDGE-and-TX_SHAPE-based-on-OFD.patch
Patch61:	0062-wifi-rtw89-avoid-inaccessible-IO-operations-during-d.patch
Patch62:	0063-wifi-rtw89-enable-mac80211-virtual-monitor-interface.patch
Patch63:	0064-wifi-rtw89-add-HE-radiotap-for-monitor-mode.patch
Patch64:	0065-wifi-rtw89-8852b-turn-off-PoP-function-in-monitor-mo.patch
Patch65:	0066-wifi-rtw89-rfk-rename-rtw89_mcc_info-to-rtw89_rfk_mc.patch
Patch66:	0067-wifi-rtw89-check-if-atomic-before-queuing-c2h.patch
Patch67:	0068-wifi-rtw89-introduce-helpers-to-wait-complete-on-con.patch
Patch68:	0069-wifi-rtw89-mac-process-MCC-related-C2H.patch
Patch69:	0070-wifi-rtw89-fw-implement-MCC-related-H2C.patch
Patch70:	0071-wifi-rtw89-link-rtw89_vif-and-chanctx-stuffs.patch
Patch71:	0072-wifi-rtw89-don-t-request-partial-firmware-if-SECURIT.patch
Patch72:	0073-wifi-rtw89-request-full-firmware-only-once-if-it-s-e.patch
Patch73:	0074-wifi-rtw89-add-mac-TSF-sync-function.patch
Patch74:	0075-wifi-rtw89-stop-mac-port-function-when-stop_ap.patch
Patch75:	0076-wifi-rtw89-fix-unsuccessful-interface_add-flow.patch
Patch76:	0077-wifi-rtw89-add-join-info-upon-create-interface.patch
Patch77:	0078-wifi-rtw89-consider-ER-SU-as-a-TX-capability.patch
Patch78:	0079-wifi-rtw89-fw-adapt-to-new-firmware-format-of-securi.patch
Patch79:	0080-wifi-rtw89-8852c-rfk-correct-DACK-setting.patch
Patch80:	0081-wifi-rtw89-8852c-rfk-correct-DPK-settings.patch
Patch81:	0082-wifi-rtw89-8852c-rfk-recover-RX-DCK-failure.patch
Patch82:	0083-wifi-rtw89-coex-add-BTC-format-version-derived-from-.patch
Patch83:	0084-wifi-rtw89-coex-use-new-introduction-BTC-version-for.patch
Patch84:	0085-wifi-rtw89-coex-Enable-Bluetooth-report-when-show-de.patch
Patch85:	0086-wifi-rtw89-coex-Update-BTC-firmware-report-bitmap-de.patch
Patch86:	0087-wifi-rtw89-coex-Add-v2-BT-AFH-report-and-related-var.patch
Patch87:	0088-wifi-rtw89-coex-refactor-_chk_btc_report-to-extend-m.patch
Patch88:	0089-wifi-rtw89-coex-Change-TDMA-related-logic-to-version.patch
Patch89:	0090-wifi-rtw89-8852b-update-BSS-color-mapping-register.patch
Patch90:	0091-wifi-rtw89-refine-6-GHz-scanning-dwell-time.patch
Patch91:	0092-wifi-rtw89-8852c-rfk-refine-AGC-tuning-flow-of-DPK-f.patch
Patch92:	0093-wifi-rtw89-Fix-a-typo-in-debug-message.patch
Patch93:	0094-wifi-rtw89-coex-Remove-le32-to-CPU-translator-at-fir.patch
Patch94:	0095-wifi-rtw89-coex-Rename-BTC-firmware-cycle-report-by-.patch
Patch95:	0096-wifi-rtw89-coex-Add-v4-version-firmware-cycle-report.patch
Patch96:	0097-wifi-rtw89-coex-Change-firmware-control-report-to-ve.patch
Patch97:	0098-wifi-rtw89-coex-Add-v5-firmware-control-report.patch
Patch98:	0099-wifi-rtw89-coex-only-read-Bluetooth-counter-of-repor.patch
Patch99:	0100-wifi-rtw89-coex-Update-WiFi-role-info-H2C-report.patch
Patch100:	0101-wifi-rtw89-coex-Add-version-code-for-Wi-Fi-firmware-.patch
Patch101:	0102-wifi-rtw89-coex-Change-Wi-Fi-Null-data-report-to-ver.patch
Patch102:	0103-wifi-rtw89-coex-Change-firmware-steps-report-to-vers.patch
Patch103:	0104-wifi-rtw89-coex-refactor-debug-log-of-slot-list.patch
Patch104:	0105-wifi-rtw89-coex-Packet-traffic-arbitration-hardware-.patch
Patch105:	0106-wifi-rtw89-coex-Change-RTL8852B-use-v1-TDMA-policy.patch
Patch106:	0107-wifi-rtw89-coex-Change-Wi-Fi-role-info-related-logic.patch
Patch107:	0108-wifi-rtw89-fix-null-vif-pointer-when-get-management-.patch
Patch108:	0109-wifi-rtw89-set-the-correct-mac_id-for-management-fra.patch
Patch109:	0110-wifi-rtw89-correct-register-definitions-of-digital-C.patch
Patch110:	0111-wifi-rtw89-8852c-rfk-correct-ADC-clock-settings.patch
Patch111:	0112-wifi-rtw89-fix-assignation-of-TX-BD-RAM-table.patch
Patch112:	0113-wifi-rtw89-8852b-fill-the-missing-configuration-abou.patch
Patch113:	0114-wifi-rtw89-coex-Update-Wi-Fi-external-control-TDMA-p.patch
Patch114:	0115-wifi-rtw89-coex-Clear-Bluetooth-HW-PTA-counter-when-.patch
Patch115:	0116-wifi-rtw89-coex-Force-to-update-TDMA-parameter-when-.patch
Patch116:	0117-wifi-rtw89-coex-Refine-coexistence-log.patch
Patch117:	0118-wifi-rtw89-coex-Set-Bluetooth-background-scan-PTA-re.patch
Patch118:	0119-wifi-rtw89-coex-Correct-A2DP-exist-variable-source.patch
Patch119:	0120-wifi-rtw89-coex-Fix-test-fail-when-coexist-with-rasp.patch
Patch120:	0121-wifi-rtw89-coex-Update-Wi-Fi-Bluetooth-coexistence-v.patch
Patch121:	0122-wifi-rtw89-correct-unit-for-port-offset-and-refine-m.patch
Patch122:	0123-wifi-rtw89-split-out-generic-part-of-rtw89_mac_port_.patch
Patch123:	0124-wifi-rtw89-mac-add-function-to-get-TSF.patch
Patch124:	0125-wifi-rtw89-debug-avoid-invalid-access-on-RTW89_DBG_S.patch
Patch125:	0126-wifi-rtw89-deal-with-RXI300-error.patch
Patch126:	0127-wifi-rtw89-fix-parsing-offset-for-MCC-C2H.patch
Patch127:	0128-wifi-rtw89-refine-MCC-C2H-debug-logs.patch
Patch128:	0129-wifi-rtw89-disallow-enter-PS-mode-after-create-TDLS-.patch
Patch129:	0130-wifi-rtw89-fix-potential-wrong-mapping-for-pkt-offlo.patch
Patch130:	0131-wifi-rtw89-refine-packet-offload-flow.patch
Patch131:	0132-wifi-rtw89-add-use-of-pkt_list-offload-to-debug-entr.patch
Patch132:	0133-wifi-rtw89-8852b-reset-IDMEM-mode-to-default-value.patch
Patch133:	0134-wifi-rtw89-8852b-don-t-support-LPS-PG-mode-after-fir.patch
Patch134:	0135-wifi-rtw89-8852b-try-to-use-NORMAL_CE-type-firmware-.patch
Patch135:	0136-wifi-rtw89-8852be-enable-CLKREQ-of-PCI-capability.patch
Patch136:	0137-wifi-rtw89-use-passed-channel-in-set_tx_shape_dfir.patch
Patch137:	0138-wifi-rtw89-8852b-correct-register-mask-name-of-TX-po.patch
Patch138:	0139-wifi-rtw89-phy-set-TX-power-according-to-RF-path-num.patch
Patch139:	0140-wifi-rtw89-use-readable-return-0-in-rtw89_mac_cfg_pp.patch
Patch140:	0141-wifi-rtw89-move-H2C-of-del_pkt_offload-before-pollin.patch
Patch141:	0142-wifi-rtw89-fix-AP-mode-authentication-transmission-f.patch
Patch142:	9000-add-driver-version.patch
Patch143:	9001-enable-Makefile-config.patch
Patch144:	9000-enable-Makefile-config.patch

%define findpat %( echo "%""P" )
%define __find_requires /usr/lib/rpm/redhat/find-requires.ksyms
%define __find_provides /usr/lib/rpm/redhat/find-provides.ksyms %{kmod_name} %{?epoch:%{epoch}:}%{version}-%{release}
%define sbindir %( if [ -d "/sbin" -a \! -h "/sbin" ]; then echo "/sbin"; else echo %{_sbindir}; fi )
%define dup_state_dir %{_localstatedir}/lib/rpm-state/kmod-dups
%define kver_state_dir %{dup_state_dir}/kver
%define kver_state_file %{kver_state_dir}/%{kmod_kernel_version}.%(arch)
%define dup_module_list %{dup_state_dir}/rpm-kmod-%{kmod_name}-modules

Name:		kmod-redhat-rtw89
Version:	%{kmod_driver_version}
Release:	%{kmod_rpm_release}%{?dist}
%if "%{kmod_driver_epoch}" != ""
Epoch:		%{kmod_driver_epoch}
%endif
Summary:	rtw89 kernel module for Driver Update Program
Group:		System/Kernel
License:	GPLv2
URL:		https://www.kernel.org/
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:	%kernel_devel_pkg = %kmod_kernel_version
%if "%{kmod_dist_build_deps}" != ""
BuildRequires:	%{kmod_dist_build_deps}
%endif
ExclusiveArch:	x86_64
%global kernel_source() /usr/src/kernels/%{kmod_kernel_version}.$(arch)

%global _use_internal_dependency_generator 0
%if "%{?kmod_kernel_version_min}" != ""
Provides:	%kernel_modules_pkg >= %{kmod_kernel_version_min}.%{_target_cpu}
%else
Provides:	%kernel_modules_pkg = %{kmod_kernel_version_dep}.%{_target_cpu}
%endif
Provides:	kmod-%{kmod_name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires(post):	%{sbindir}/weak-modules
Requires(postun):	%{sbindir}/weak-modules
Requires:	kernel >= 5.14.0-284
%if 0
Requires: firmware(%{kmod_name}) = ENTER_FIRMWARE_VERSION
%endif
%if "%{kmod_build_dependencies}" != ""
BuildRequires:  %{kmod_build_dependencies}
%endif
%if "%{kmod_dependencies}" != ""
Requires:       %{kmod_dependencies}
%endif
%if "%{kmod_provides}" != ""
Provides:       %{kmod_provides}
%endif
# if there are multiple kmods for the same driver from different vendors,
# they should conflict with each other.
Conflicts:	kmod-%{kmod_name}

%description
rtw89 kernel module for Driver Update Program

%if 0

%package -n kmod-redhat-rtw89-firmware
Version:	ENTER_FIRMWARE_VERSION
Summary:	rtw89 firmware for Driver Update Program
Provides:	firmware(%{kmod_name}) = ENTER_FIRMWARE_VERSION
%if "%{kmod_kernel_version_min}" != ""
Provides:	%kernel_modules_pkg >= %{kmod_kernel_version_min}.%{_target_cpu}
%else
Provides:	%kernel_modules_pkg = %{kmod_kernel_version_dep}.%{_target_cpu}
%endif
%description -n  kmod-redhat-rtw89-firmware
rtw89 firmware for Driver Update Program


%files -n kmod-redhat-rtw89-firmware
%defattr(644,root,root,755)
%{FIRMWARE_FILES}

%endif

# Development package
%if 0%{kmod_devel_package}
%package -n kmod-redhat-rtw89-devel
Version:	%{kmod_driver_version}
Summary:	rtw89 development files for Driver Update Program

%description -n  kmod-redhat-rtw89-devel
rtw89 development files for Driver Update Program


%files -n kmod-redhat-rtw89-devel
%defattr(644,root,root,755)
/lib/modules/%{kmod_rpm_name}-%{kmod_driver_version}/
%endif

# Extra files package
%if 0%{kmod_files_package}
%package -n kmod-redhat-rtw89-files
Version:	%{kmod_driver_version}
Summary:	rtw89 additional files for Driver Update Program
%if 0%{kmod_files_noarch}
BuildArch:	noarch
%endif
%if "%{?kmod_kernel_version_min}" != ""
Provides:	%kernel_modules_pkg >= %{kmod_kernel_version_min}.%{_target_cpu}
%else
Provides:	%kernel_modules_pkg = %{kmod_kernel_version_dep}.%{_target_cpu}
%endif

%description -n  kmod-redhat-rtw89-files
rtw89 additional files for Driver Update Program


%files -n kmod-redhat-rtw89-files
%defattr(644,root,root,755)


%endif

%post
modules=( $(find /lib/modules/%{kmod_kernel_version}.%(arch)/%{kmod_install_path} | grep '\.ko$') )
printf '%s\n' "${modules[@]}" | %{sbindir}/weak-modules --add-modules --no-initramfs

mkdir -p "%{kver_state_dir}"
touch "%{kver_state_file}"

exit 0

%posttrans
# We have to re-implement part of weak-modules here because it doesn't allow
# calling initramfs regeneration separately
if [ -f "%{kver_state_file}" ]; then
	kver_base="%{kmod_kernel_version_dep}"
	kvers=$(ls -d "/lib/modules/${kver_base%%.*}"*)

	for k_dir in $kvers; do
		k="${k_dir#/lib/modules/}"

		tmp_initramfs="/boot/initramfs-$k.tmp"
		dst_initramfs="/boot/initramfs-$k.img"

		# The same check as in weak-modules: we assume that the kernel present
		# if the symvers file exists.
		if [ -e "/boot/symvers-$k.gz" ] || [ -e "$k_dir/symvers.gz" ]; then
			/usr/bin/dracut -f "$tmp_initramfs" "$k" || exit 1
			cmp -s "$tmp_initramfs" "$dst_initramfs"
			if [ "$?" = 1 ]; then
				mv "$tmp_initramfs" "$dst_initramfs"
			else
				rm -f "$tmp_initramfs"
			fi
		fi
	done

	rm -f "%{kver_state_file}"
	rmdir "%{kver_state_dir}" 2> /dev/null
fi

rmdir "%{dup_state_dir}" 2> /dev/null

exit 0

%preun
if rpm -q --filetriggers kmod 2> /dev/null| grep -q "Trigger for weak-modules call on kmod removal"; then
	mkdir -p "%{kver_state_dir}"
	touch "%{kver_state_file}"
fi

mkdir -p "%{dup_state_dir}"
rpm -ql kmod-redhat-rtw89-%{kmod_driver_version}-%{kmod_rpm_release}%{?dist}.$(arch) | \
	grep '\.ko$' > "%{dup_module_list}"

%postun
if rpm -q --filetriggers kmod 2> /dev/null| grep -q "Trigger for weak-modules call on kmod removal"; then
	initramfs_opt="--no-initramfs"
else
	initramfs_opt=""
fi

modules=( $(cat "%{dup_module_list}") )
rm -f "%{dup_module_list}"
printf '%s\n' "${modules[@]}" | %{sbindir}/weak-modules --remove-modules $initramfs_opt

rmdir "%{dup_state_dir}" 2> /dev/null

exit 0

%files
%defattr(644,root,root,755)
/lib/modules/%{kmod_kernel_version}.%(arch)
/etc/depmod.d/%{kmod_name}.conf
%doc /usr/share/doc/%{kmod_rpm_name}/greylist.txt
%if !0%{kmod_files_package}


%endif

%prep
%setup -n %{kmod_name}-%{kmod_vendor}-%{kmod_driver_version}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch87 -p1
%patch88 -p1
%patch89 -p1
%patch90 -p1
%patch91 -p1
%patch92 -p1
%patch93 -p1
%patch94 -p1
%patch95 -p1
%patch96 -p1
%patch97 -p1
%patch98 -p1
%patch99 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1
%patch118 -p1
%patch119 -p1
%patch120 -p1
%patch121 -p1
%patch122 -p1
%patch123 -p1
%patch124 -p1
%patch125 -p1
%patch126 -p1
%patch127 -p1
%patch128 -p1
%patch129 -p1
%patch130 -p1
%patch131 -p1
%patch132 -p1
%patch133 -p1
%patch134 -p1
%patch135 -p1
%patch136 -p1
%patch137 -p1
%patch138 -p1
%patch139 -p1
%patch140 -p1
%patch141 -p1
%patch142 -p1
%patch143 -p1
%patch144 -p1
set -- *
mkdir source
mv "$@" source/
mkdir obj

%build
rm -rf obj
cp -r source obj

PWD_PATH="$PWD"
%if "%{workaround_no_pwd_rel_path}" != "1"
PWD_PATH=$(realpath --relative-to="%{kernel_source}" . 2>/dev/null || echo "$PWD")
%endif
%{make_build} -C %{kernel_source} V=1 M="$PWD_PATH/obj/%{kmod_kbuild_dir}" \
	NOSTDINC_FLAGS="-I$PWD_PATH/obj/include -I$PWD_PATH/obj/include/uapi %{nil}" \
	EXTRA_CFLAGS="%{nil}" \
	%{nil}
# mark modules executable so that strip-to-file can strip them
find obj/%{kmod_kbuild_dir} -name "*.ko" -type f -exec chmod u+x '{}' +

kabilist="/lib/modules/kabi-current/kabi_%{abi_list}_%{_target_cpu}"
for modules in $( find obj/%{kmod_kbuild_dir} -name "*.ko" -type f -printf "%{findpat}\n" | sed 's|\.ko$||' | sort -u ) ; do
	# update depmod.conf
	module_weak_path=$(echo "$modules" | sed 's/[\/]*[^\/]*$//')
	if [ -z "$module_weak_path" ]; then
		module_weak_path=%{name}
	else
		module_weak_path=%{name}/$module_weak_path
	fi
	echo "override $(echo $modules | sed 's/.*\///')" \
	     "$(echo "%{kmod_kernel_version_dep}" |
	        sed 's/\.[^\.]*$//;
		     s/\([.+?^$\/\\|()\[]\|\]\)/\\\0/g').*" \
		     "weak-updates/$module_weak_path" >> source/depmod.conf

	# update greylist
	nm -u obj/%{kmod_kbuild_dir}/$modules.ko | sed 's/.*U //' |  sed 's/^\.//' | sort -u | while read -r symbol; do
		grep -q "^\s*$symbol\$" $kabilist || echo "$symbol" >> source/greylist
	done
done
sort -u source/greylist | uniq > source/greylist.txt

%install
export INSTALL_MOD_PATH=$RPM_BUILD_ROOT
export INSTALL_MOD_DIR=%{kmod_install_path}
PWD_PATH="$PWD"
%if "%{workaround_no_pwd_rel_path}" != "1"
PWD_PATH=$(realpath --relative-to="%{kernel_source}" . 2>/dev/null || echo "$PWD")
%endif
make -C %{kernel_source} modules_install \
	M=$PWD_PATH/obj/%{kmod_kbuild_dir}
# Cleanup unnecessary kernel-generated module dependency files.
find $INSTALL_MOD_PATH/lib/modules -iname 'modules.*' -exec rm {} \;

install -m 644 -D source/depmod.conf $RPM_BUILD_ROOT/etc/depmod.d/%{kmod_name}.conf
install -m 644 -D source/greylist.txt $RPM_BUILD_ROOT/usr/share/doc/%{kmod_rpm_name}/greylist.txt
%if 0
%{FIRMWARE_FILES_INSTALL}
%endif
%if 0%{kmod_devel_package}
install -m 644 -D $PWD/obj/%{kmod_kbuild_dir}/Module.symvers $RPM_BUILD_ROOT/lib/modules/%{kmod_rpm_name}-%{kmod_driver_version}/build/Module.symvers

if [ -n "%{kmod_devel_src_paths}" ]; then
	for i in %{kmod_devel_src_paths}; do
		mkdir -p "$RPM_BUILD_ROOT/lib/modules/%{kmod_rpm_name}-%{kmod_driver_version}/build/$(dirname "$i")"
		cp -rv "$PWD/source/$i" \
			"$RPM_BUILD_ROOT/lib/modules/%{kmod_rpm_name}-%{kmod_driver_version}/build/$i"
	done
fi
%endif



%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Jun 27 2023 Eugene Syromiatnikov <esyr@redhat.com> 5.14.0_284.11.1_dup9.2-1
- c8eb14f582ef9c529860817fbe91ba1a6a270315
- rtw89 kernel module for Driver Update Program
- Resolves: #bz2214527
