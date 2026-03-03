from base64 import b64decode, b64encode
from hashlib import scrypt
from os import urandom


def password_hash(data: str, salt: bytes | None = None, cost: int = 10) -> str:
    """
    Gera um hash no formato $7$<cost>$<salt>$<hash>

    :param data: Senha para gerar hash.
    :param salt: Salt (parâmetro salt)
    :param cost: Custo de CPU/Memória (parâmetro n)
    :return: Hash gerado.
    """
    salt = urandom(16) if salt is None else salt
    hash_data = scrypt(data.encode(), salt=salt, n=1 << cost, r=8, p=1, dklen=64)

    return f"$7${cost}${b64encode(salt).decode('ascii')}${b64encode(hash_data).decode('ascii')}"


def password_verify(hash_data: str, data: str) -> bool:
    """
    Verifica um hash no formato $7$<cost$<salt$<hash>

    :param hash_data: Hash gerado.
    :param data: Senha para verificar hash.
    :return: Se a senha bate com o hash gerado.
    """
    _, version, cost, salt, _ = hash_data.split("$", 5)
    if version != "7":
        return False

    computed_hash = password_hash(data=data, salt=b64decode(salt.encode("ascii")), cost=int(cost))
    return computed_hash == hash_data
