%define kmod_name		rtw89
%define kmod_vendor		redhat
%define kmod_rpm_name		kmod-redhat-rtw89
%define kmod_driver_version	4.18.0_363_dup8.5
%define kmod_driver_epoch	%{nil}
%define kmod_rpm_release	1
%define kmod_kernel_version	4.18.0-348.el8
%define kmod_kernel_version_min	%{nil}
%define kmod_kernel_version_dep	%{nil}
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

%{!?dist: %define dist .el8_5}
%{!?make_build: %define make_build make}

%if "%{kmod_kernel_version_dep}" == ""
%define kmod_kernel_version_dep %{kmod_kernel_version}
%endif

%if "%{kmod_dist_build_deps}" == ""
%if (0%{?rhel} > 7) || (0%{?centos} > 7)
%define kmod_dist_build_deps redhat-rpm-config kernel-abi-whitelists elfutils-libelf-devel kernel-rpm-macros kmod
%else
%define kmod_dist_build_deps redhat-rpm-config kernel-abi-whitelists
%endif
%endif

Source0:	%{kmod_name}-%{kmod_vendor}-%{kmod_driver_version}.tar.bz2
# Source code patches
Patch0:	0001-rtw89-add-Realtek-802.11ax-driver.patch
Patch1:	0002-rtw89-Fix-two-spelling-mistakes-in-debug-messages.patch
Patch2:	0003-rtw89-Remove-redundant-check-of-ret-after-call-to-rt.patch
Patch3:	0004-rtw89-fix-return-value-check-in-rtw89_cam_send_sec_k.patch
Patch4:	0005-rtw89-remove-unneeded-semicolon.patch
Patch5:	0006-rtw89-fix-error-function-parameter.patch
Patch6:	0007-rtw89-remove-duplicate-register-definitions.patch
Patch7:	0008-rtw89-fix-return-value-in-hfc_pub_cfg_chk.patch
Patch8:	0009-rtw89-Fix-variable-dereferenced-before-check-sta.patch
Patch9:	0010-rtw89-update-partition-size-of-firmware-header-on-sk.patch
Patch10:	0011-rtw89-fill-regd-field-of-limit-limit_ru-tables-by-en.patch
Patch11:	0012-rtw89-update-rtw89-regulation-definition-to-R58-R31.patch
Patch12:	0013-rtw89-update-tx-power-limit-limit_ru-tables-to-R54.patch
Patch13:	0014-rtw89-update-rtw89_regulatory-map-to-R58-R31.patch
Patch14:	0015-rtw89-remove-unnecessary-conditional-operators.patch
Patch15:	0016-rtw89-remove-unneeded-variable.patch
Patch16:	0017-rtw89-fix-potentially-access-out-of-range-of-RF-regi.patch
Patch17:	0018-rtw89-add-AXIDMA-and-TX-FIFO-dump-in-mac_mem_dump.patch
Patch18:	0019-rtw89-add-const-in-the-cast-of-le32_get_bits.patch
Patch19:	0020-rtw89-use-inline-function-instead-macro-to-set-H2C-a.patch
Patch20:	0021-rtw89-update-scan_mac_addr-during-scanning-period.patch
Patch21:	0022-rtw89-fix-incorrect-channel-info-during-scan.patch
Patch22:	0023-rtw89-fix-sending-wrong-rtwsta-mac_id-to-firmware-to.patch
Patch23:	0024-rtw89-remove-cch_by_bw-which-is-not-used.patch
Patch24:	0025-rtw89-don-t-kick-off-TX-DMA-if-failed-to-write-skb.patch
Patch25:	0026-rtw89-coex-correct-C2H-header-length.patch
Patch26:	0027-rtw89-coex-Not-to-send-H2C-when-WL-not-ready-and-cou.patch
Patch27:	0028-rtw89-coex-Add-MAC-API-to-get-BT-polluted-counter.patch
Patch28:	0029-rtw89-coex-Define-LPS-state-for-BTC-using.patch
Patch29:	0030-rtw89-coex-Update-BT-counters-while-receiving-report.patch
Patch30:	0031-rtw89-coex-Cancel-PS-leaving-while-C2H-comes.patch
Patch31:	0032-rtw89-coex-Update-COEX-to-5.5.8.patch
Patch32:	0033-rtw89-8852a-correct-bit-definition-of-dfs_en.patch
Patch33:	0034-rtw89-fix-maybe-uninitialized-error-RHEL-only.patch
Patch34:	0035-rtw89-enable-driver-and-device-RTL8852AE.patch
Patch35:	0036-rtw89-fix-maybe-uninitialized-error.patch
Patch36:	9000-force-enable-rtw89.patch
Patch37:	9001-add-driver-version.patch
Patch38:	9002-change-firmware-path.patch

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
Requires:	kernel >= 4.18.0-348.el8

Requires:	kernel < 4.18.0-349.el8
%if 1
Requires: firmware(%{kmod_name}) = 20211119_105.gitf5d51956_dup8.5
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

%if 1

%package -n kmod-redhat-rtw89-firmware
Version:	20211119_105.gitf5d51956_dup8.5
Summary:	rtw89 firmware for Driver Update Program
Provides:	firmware(%{kmod_name}) = 20211119_105.gitf5d51956_dup8.5
%if "%{kmod_kernel_version_min}" != ""
Provides:	%kernel_modules_pkg >= %{kmod_kernel_version_min}.%{_target_cpu}
%else
Provides:	%kernel_modules_pkg = %{kmod_kernel_version_dep}.%{_target_cpu}
%endif
%description -n  kmod-redhat-rtw89-firmware
rtw89 firmware for Driver Update Program


%files -n kmod-redhat-rtw89-firmware
%defattr(644,root,root,755)
/lib/firmware/rtw89/rtw8852a_fw_dup85.bin


%endif

# Development package
%if 0%{kmod_devel_package}
%package -n kmod-redhat-rtw89-devel
Version:	%{kmod_driver_version}
Requires:	kernel >= 4.18.0-348.el8

Requires:	kernel < 4.18.0-349.el8
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
/etc/dracut.conf.d/kmod-redhat-rtw89_dup85.conf
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
/etc/dracut.conf.d/kmod-redhat-rtw89_dup85.conf
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

whitelist="/lib/modules/kabi-current/kabi_whitelist_%{_target_cpu}"
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
		grep -q "^\s*$symbol\$" $whitelist || echo "$symbol" >> source/greylist
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
%if 1
install -m 644 -D source/firmware/rtw89/rtw8852a_fw_dup85.bin $RPM_BUILD_ROOT/lib/firmware/rtw89/rtw8852a_fw_dup85.bin

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
install -m 664 -D source/extra//etc/dracut.conf.d/kmod-redhat-rtw89_dup85.conf $RPM_BUILD_ROOT//etc/dracut.conf.d/kmod-redhat-rtw89_dup85.conf


%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Feb 09 2022 Eugene Syromiatnikov <esyr@redhat.com> 4.18.0_363_dup8.5-1
- 9dc660bf1362f5a22a908e61004498cf7ec063a8
- rtw89 kernel module for Driver Update Program
- Resolves: #bz2051886
