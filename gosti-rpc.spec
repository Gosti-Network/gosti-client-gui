# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['gosti-rpc.py'],
    pathex=[],
    binaries=[],
    datas=[('../../chia-blockchain/chia/wallet/puzzles/*', 'chia/wallet/puzzles/'), ('../../chia-blockchain/chia/wallet/util/*', 'chia/wallet/util/'), ('../../chia-blockchain/chia/wallet/vc_wallet/vc_puzzles*', 'chia/wallet/vc_wallet/vc_puzzles/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='gosti-rpc',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
