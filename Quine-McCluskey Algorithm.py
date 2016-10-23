# -----------------------------------------------------------------------
#   Quine-McCluskey Algorith
#
#   Author:         Corona, Ansël
#   Student ID:     2014-0031
#   Date:           19/07/2016
# ----------------------------------------------------------------------
def int_to_str(num_bits, i):
    x = ['1' if i & (1 << k) else '0' for k in range(num_bits - 1, -1, -1)]
    return "".join(x)


def extract_prime_implicants(num_bits, mini_terms, x_mini_terms=None):
    if x_mini_terms is None:
        x_mini_terms = []
    total_terms = mini_terms + x_mini_terms
    if len(total_terms) == 0:
        return None

    mini_terms = set(int_to_str(num_bits, x) for x in mini_terms)
    x_mini_terms = set(int_to_str(num_bits, x) for x in x_mini_terms)

    total_terms = mini_terms | x_mini_terms
    if len(total_terms) == 0:
        return None

    prime_implicants = get_implicants(num_bits, total_terms)

    return prime_implicants


def get_implicants(num_bits, total_terms):
    sets = num_bits + 1
    implicants = set()

    groups = [set() for i in range(sets)]
    for term in total_terms:
        bits_on = term.count('1')
        groups[bits_on].add(term)

    all_done = False
    while not all_done:
        groups = dict()
        for term in total_terms:
            b_on = term.count('1')
            if b_on not in groups:
                groups[b_on] = set()
            groups[b_on].add(term)

        total_terms = set()
        used_terms = set()

        for ind in groups:
            next_ind = ind + 1
            if next_ind in groups:
                group_next = groups[next_ind]
                for term1 in groups[ind]:

                    for i, x in enumerate(term1):
                        if x == '0':
                            term2 = term1[:i] + '1' + term1[i + 1:]
                            if term2 in group_next:
                                merged_term = term1[:i] + '-' + term1[i + 1:]
                                used_terms.add(term1)
                                used_terms.add(term2)
                                total_terms.add(merged_term)

        for g in list(groups.values()):
            implicants |= g - used_terms

        if len(used_terms) == 0:
            all_done = True

    for g in list(groups.values()):
        implicants |= g
    return implicants


def get_essential_implicants(num_bits, mini_terms, x_mini_terms):
    comb = {}
    for term in mini_terms:
        comb[term] = set(p for p in combinations(term) if p not in x_mini_terms)

    essentials_range = set()
    essential_implicants = set()
    groups = dict()

    for term in mini_terms:
        x = get_range(term, len(comb[term]))
        if x not in groups:
            groups[x] = set()
        groups[x].add(term)
    for term in sorted(list(groups.keys()), reverse=True):
        for g in groups[term]:
            if not comb[g] <= essentials_range:
                essential_implicants.add(g)
                essentials_range |= comb[g]
    if len(essential_implicants) == 0:
        essential_implicants = ('-' * num_bits)
    return essential_implicants


def get_range(terms, range):
    x = 0
    for term in terms:
        if term == "-":
            x += 8
        elif term == "1":
            x += 1
    return x + range * 4


def combinations(value=''):
    num_bits = len(value)
    result = ['0' for i in range(num_bits)]
    i = 0
    direction = +1

    while i >= 0:
        if value[i] == '0' or value[i] == '1':
            result[i] = value[i]
        elif value[i] == '-':
            if direction == +1:
                result[i] = '0'
            elif result[i] == '0':
                result[i] = '1'
                direction = +1
        i += direction
        if i == num_bits:
            direction = -1
            i = num_bits - 1
            yield "".join(result)


def main():
    num_bits = int(input())
    mini_terms = [int(x) for x in input().split()]
    x_mini_terms = [int(x) for x in input().split()]

    primes = extract_prime_implicants(num_bits, mini_terms, x_mini_terms)
    essential_primes = get_essential_implicants(num_bits, primes, x_mini_terms)

    print(primes)
    print(essential_primes)


if __name__ == '__main__':
    main()
