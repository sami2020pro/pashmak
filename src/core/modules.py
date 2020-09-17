
import hashlib
modules = {}

modules["process"] = """# hello some thing

mem 'hello'; out ^;

"""
modules["hash"] = """
alias hash_sha256;
	set $tmp_hash_sha256_value; copy $tmp_hash_sha256_value;
	mem 'import hashlib\nself.mem = hashlib.sha256("' + $tmp_hash_sha256_value + '".encode()).hexdigest()'; python ^;
	free $tmp_hash_sha256_value;
endalias;

alias hash_md5;
	set $tmp_hash_md5_value; copy $tmp_hash_md5_value;
	mem 'import hashlib\nself.mem = hashlib.md5("' + $tmp_hash_md5_value + '".encode()).hexdigest()'; python ^;
	free $tmp_hash_md5_value;
endalias;
"""