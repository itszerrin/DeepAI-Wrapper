import js2py

from Types import MyRandomString

def get_random_str() -> MyRandomString:

    """
    This function returns a random string in the hardcoded JS
    """

    _random_str = """
const myrandomstr = function () {
    return Math.round(Math.random() * 100000000000) + '';
};

"""

    return js2py.eval_js(_random_str + "myrandomstr()")

# their hashing function, deobfuscated
def get_hash(useragent: str, r_string: MyRandomString) -> str:

    """
    This function returns the hash composed of the random string and the user agent
    """

    _hash_func_js = """
const myhashfunction = (function () {
  for (var a = [], b = 0; 64 > b; )
    a[b] = 0 | (4294967296 * Math.sin(++b % Math.PI));
  return function (c) {
    var d,
      e,
      f,
      g = [(d = 1732584193), (e = 4023233417), ~d, ~e],
      h = [],
      l = unescape(encodeURI(c)) + '',
      k = l.length;
    c = (--k / 4 + 2) | 15;
    for (h[--c] = 8 * k; ~k; ) h[k >> 2] |= l.charCodeAt(k) << (8 * k--);
    for (b = l = 0; b < c; b += 16) {
      for (
        k = g;
        64 > l;
        k = [
          (f = k[3]),
          d +
            (((f =
              k[0] +
              [(d & e) | (~d & f), (f & d) | (~f & e), d ^ e ^ f, e ^ (d | ~f)][
                (k = l >> 4)
              ] +
              a[l] +
              ~~h[b | ([l, 5 * l + 1, 3 * l + 5, 7 * l][k] & 15)]) <<
              (k = [7, 12, 17, 22, 5, 9, 14, 20, 4, 11, 16, 23, 6, 10, 15, 21][
                4 * k + (l++ % 4)
              ])) |
              (f >>> -k)),
          d,
          e,
        ]
      )
        (d = k[1] | 0), (e = k[2]);
      for (l = 4; l; ) g[--l] += k[l];
    }
    for (c = ''; 32 > l; )
      c += ((g[l >> 3] >> (4 * (1 ^ l++))) & 15).toString(16);
    return c.split('').reverse().join('');
  };
})();

function call_hash_func() {
    return myhashfunction("uagoeshere" + myhashfunction("uagoeshere" + myhashfunction("uagoeshere" + "myrandomstr" + "x")));
}
""".replace("myrandomstr", r_string).replace("uagoeshere", useragent)

    return js2py.eval_js(_hash_func_js + "call_hash_func()")

__all__ = [
    'get_random_str',
    'get_hash'
]
