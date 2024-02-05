# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['gym.py'],
    pathex=[],
    binaries=[],
    datas=[('./test_images', 'test_images'), ('./employee_qrcodes', 'employee_qrcodes'), ('./frame_2_icons', 'frame_2_icons'), ('./frame_3_icons', 'frame_3_icons'), ('./frame_4_icons', 'frame_4_icons'), ('./frame_5_icons', 'frame_5_icons'), ('./frame_6_icons', 'frame_6_icons'), ('./frame_7_icons', 'frame_7_icons'), ('./member_qrcodes', 'member_qrcodes'), ('./trainer_qrcodes', 'trainer_qrcodes'), ('./enquiry_qrcodes', 'enquiry_qrcodes'), ('./member_photo', 'member_photo')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='gym',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='gym',
)
