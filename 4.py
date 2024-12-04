def find_xmas(table):
    count = 0
    rows = len(table)
    cols = len(table[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    for i in range(rows):
        for j in range(cols):
            if table[i][j] == 'X':
                for direction in directions:
                    found = True
                    for k in range(4):
                        ni, nj = i + direction[0] * k, j + direction[1] * k
                        if ni < 0 or ni >= rows or nj < 0 or nj >= cols or table[ni][nj] != 'XMAS'[k]:
                            found = False
                            break
                    if found:
                        count += 1

    return count

def find_x_mas(table):
    count = 0
    rows = len(table)
    cols = len(table[0])

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if not table[i][j] == 'A':
                continue
            check = table[i-1][j-1] + table[i-1][j+1] + table[i+1][j-1] + table[i+1][j+1]
            if check.count('M') == 2 and check.count('S') == 2 and check[0] != check[3]:
                count += 1

    return count

table = [
    "SSSMMAASASAMXSSMSMMSSSSSSMSSMMMSMSAXMAMASXXXXMXMXSXXXMAMMSSSSSSXXAMXMSSXMAXMMXMMSSSMSAMXMXSXMSMSSSXMMSAMMSAMXMSMMMXSASMMMXMXMMXXAMXXMASXMXMS",
    "AMAASMMSASASAAMMAAXXAAXAAAAXASAAXSAMXSXASMSMAMSMASMSMXAXSAMXAAAMSXXAMXAAMXSAMAAXSAAAMAMAMASMMAASAXSAASAMXAAXAXAMAXXXAXAASMMASMASXMSXSAMAMMMS",
    "MSSMMAAXASAMXMMSSSMMMMMMMMMXAMMMMSAMAMMXMAMSAMAMXSAAASMMMASMMMMMAASXSMSAMXAASXSMMMMMSAMMMASASMSMAMMMMSAXMSMSMSMSMSMMMMSMXAXASXAAAMAMMASAMAAM",
    "XXAMXMMMMMMMMXXAAAXMSAMXSXMASXSXXSAMXSSXMAMXMSMXAMMMXAMXSAMAMAXMMXMXAMXAAMMXMAAMXAAXXXSXMASMMMMMXMMMASAMXXXXXAXAMAMAAAMMSSMASMSSSMASXXMXSMSX",
    "MMMMSMMMXMSASAMMXMXMMMXAMAMXXAMMXXXXSAMXSAMAMAMXMASMSMAXMASMMXSAMAMSSMMMMXXXMMMMMXSSMSMAMASXMASMMSXMASMAMMMSXMSXSASXSMSAAAMSMMAAAMMMXXAAXAMA",
    "AAAAAAAMAMXASMXAASXSAAMSSMMSMAMMAMSMMAXXAMSMSASMSMXXAMSAXXAAAASMMXXAMXASASXMMASASAAXMASAMASASASAMXSMASMSAAAAAXMXMASMMAMMSSMXAMMMMMMASMXMMAMM",
    "SSMSSSMSASMAMXMSMSASMXMAAAAMXMMMAXAASAMXMMAASASAASMSXMAMSMSMMXXASXMASXXMAMXSXAXASMSMAMSXSXXXMASMMMMMXSAXMMSSMMXAMAMAMAXXAAMSMMSXMAMASAAXAAXX",
    "XXAAMAASAXMSMSAMXMMMMSMSSMMSMXSXMXSXMASXXMMXMXMXAMMAMMMMAMAMSSMAMAMAMMSMMMAMMSXMSAMXMXMMMMMXSXSAAXASMMMMSXMAMSSMXSSSSMSMSSMAAAMAXXMASXSXXXXX",
    "XMMMSMMMSMAAAMAMAAXXAXMMMAAAXMSASAMASAMMMXMXSXMMXSXSAMXSMSMSAAAMSSMAXAAMAMAMXAASMMMAAAXAAAXMSASMMMMSAAAMAXXAXMASAXXAAXXAMAMSSMSMMMSAMAMASXMS",
    "SXMAMXAAXMSMMMAMMSMMMXSMMMSSSMSAMASAMXXSXASAMXXMAMMMXMASXMXMMSMXAXSMSSMSXSASMSSMAASXSXSMSXSAMXMAMSMMMMSSMMXSMMAMMSMSMMMMSAMXAXAAAASAMSAAAAAX",
    "AAMSSSMSSXMASMMMXAMAXAAAMAMXXAMAMXMMMSAMXXMAMXXMASAMAXAMMMMSMMMMMXAMAMXAAMASXXMMSMSXMASXAAMXMAXAMAAMMMAMXAMMAMSAAMXXMAMASAMXSMSXMASXMXMASMMM",
    "MXMAAXAMMMMAMAAASMSAMMSMMMSAMMMAMMAMAMASXMSAMSXSASMSXMASXAAMMASMXXMMSSMMSMASMSXAMXMXMAMMMSMMSSSMSSMMAMASMSASAMMAMXASXSMASASXXAMXMAXMSMSAMXAA",
    "XMSMXMMXAXMAMSMMMXMASAAXAXMXMXSASXAMMSXMAMMXSMASAMASXAXXXMMMSAXMMMMAXXAXMMAXAXMXSAMMMAXXMXAMXAAXAXASXSAMXXMSXMXSXMASAAMAXXMAMAMXMASXXAXAXSSS",
    "XAAMMSMSXSMMMXASXXSAMMSMSMSXMASASXXMAMMSMMSMSMAMXMAMMSSMMSSXMMSAAAMSSSSMXMSMMMMAMAMAXMXSASXMMSSMMSXMAMMSMMAXXMAMAMAMMMMSSSMSMAMXMASAMSMMXAAX",
    "SSMSAAXAXMAMAMAMAMMAMAAAXAXMMMSASMSMAAAMXMAAMMAXXMXSMMMAAAXAAAXMMXSAAMMAAMXSXAMASXMSMSAXMMSXMAAAMXMASAAAAMMMMMASXMASMXAAAAAASMSMXSMXMAASMMSX",
    "AAXMMSAMXSXMMSSMSMSAMMSSMSMAAXMAMAXSSSSXMSMSMSXSAMASAXSSMSSMMMSMSXMMSMASXSAMXXMASXAXXMAMSAMXMXSSMXAAXMSMSMAAAXASMSSSMMMMXMMMMXAMXMAMSSSXXMAM",
    "XMMMSMMAXXMSXAAAMASXSAAXAAASXSMMMMMXMAMAAAAXXAXSAMASXMAMMXAMXXXAAAXAMXAMAMASMMSXMXSMSMAMMASXSAAAAXSXSMMXMXSXSAASAMXMXSMSXSXAMSMSMMAMAXMXMASX",
    "XMAMAASMMMAXMXMMMAMAMMSMSAMMAXMXAXMAMAMMSSMXMSMSXMASASAMMSAMXXMXSSMSSMASXXAXMAXAXMMAXMAXMXSAMMMMMMMAMASAXAXAXMSMXSAMXMAMAASMXASAASMMXSMSMAMX",
    "ASXSMXMAAMSXSXSXMASXMAMAMMMMAMSSSMSASMXMAXMMAMAMXMAMAMMSAMXMMXMAMMAXAMAAAMSMMXSASMMAMSSXSAMXMMXSAMMASAMMMMSAMXXMAXAXAMAMXMAMSMSMXMAXXAAAAASX",
    "MAAXMXMMSMMASAMXMAMAMXSAMASMMSAAAXMAMAAXAXMASMMMSSSMXMXMASXAXAMXSXXSMMSMXMMASAAAMXAAXXXAMXSMSXMMAXSXMASXAAXAMXSMSMSMSSMXAMAXSXMXSAMXSMSMSMSA",
    "XMMXAAMXMAMMMMMAMASAMXMAXAMAXAMSMSMSMSXMASXAXAAAXAAAAAMMMAMSSMSAMMMXXAMXSMSAMAMSMXSSXSMSMSMAXAMMSMSASAMMMXSXMAXSAAMXMAAXSSSMSAMXXAXAXMAMXMXM",
    "SAMXSASASAXAAMMXMASAMMSMMXSXMAXAAXAMAMXXXMMMSSMSSMXSSMXAXMAXAMMMSAMMMSSMMXMAMXXMAXXAXSAXMASXSMMMMAMAMAXXAAXXMASMMMMAXMMMXAXASXMSSMMSMMMSMXSM",
    "SAXAXASXSASXSSMSMMMAXMAXXMMMAXMMXMXMAMMSMMAAMAXAXXXMAMSSSSXMMMAAMMSAAMAMSSSSXMASMSSSMMAMSMSXXAAXMAMASXMSMMSASXMASASAMMSSMAMMMMMMAMXMASASMASA",
    "SMMSMAMAMXMXAAAXXMMSMMXXSAAAMSXMXAXMASAAAMSMSAMMXMSMAMXAXMASXSMXSASMMSAMXAAASMMMAMXAXSAMXXXXSXMMSAXXMXMXAMSAMXMMSXMASXAAMXMASASMXMASMMASMAMX",
    "XMAXMAMXMSXMSMMMMSAMASAAXMASXMAASMXSXSMMXMXASXMMMAAXAMMAMXMMAAASMMMSMMMMMMMMMMAMAMSMMMMSXMMXSMXXMXSSMMMMMMMMMMMAMAMAMMSMMMMASXXMASXSXMMMMMSS",
    "XMASMSSSMXXXASAAXMASAMMSMMXMASXMSAMSXMAXAMXXMAMXSSMSMSAAMSMMXMXMAAAMXASXMASMASAXAMAXAAASAXAAMXMMSMAXAAXAAAASAMMAXMMAXXAMXSXXMAMSMMASASMXXAAX",
    "MMMSAMAXXXMXASMMSMXMXMMAXXAMXMXAMAMMASAMMMSMSXMAXAAAMMMMMAAXMMMSSMSSMXSXMAMMAXMSSSMSSSMSAMSSMAAMAAMMXSXSSSMSASXMMAMAMSASASAMXAXSXSXMMAXMSMMS",
    "AAAMAMAMXMSAMMMMAMMSMMMSMSSSMSMMMAMSMMXSAAAAMXMXMMMMSAAXSSXMMAAXXAXXMMSXMASMMSMAMAAAAMAMAMXAXMXSMSXSAXXXAAASAMAMSSMAXSAMAMSAMXMMAAAMAMMMAAXX",
    "XMXSAMXSAAMASAXSAMXAAAAAASAAAXAMSSMMXAASMXMXMAMMSMMXMMMXAXAASMSSMSMMSASAMASAMAMASMMMMSXMAMXMMXAXMAAMASMSSMMMSMXMAAMSMMAMAMXXMAXMAMAMAXAXSSMM",
    "ASASXXXMAXSAMXMSSSXSMMSSMMXMMMXMAXAASMMSXASASASAAMASMASMAMSXMXAXAAAMMXXAMASAMMSAMXAXMSASMSMSAMMSSMAMAMAXAMXMASAMXSMXASXMXXSAMSMMMSASASMMMAAA",
    "MMASAMSXSAMXXXXMASXMAXAMXSAMXAAMXSMMXAAXMASASXSXXXASMAXMXMXXSXSMMMSXMMSMMAMAMXMASMXSASAMAAMMASAAAASMMMMSAMXSMXXSMXXMAMAMSAMMMMASXMXSAMXASMMS",
    "AMAMASAAMXSMSSXSAMXMMMAXASASMSXSAAAASMMSXXMXMASASMMMMXXMAXXXMAXAMAMAXMASMSSSMSMMMAAMMMAMMMXSAMMSMMXASAASAMMSXSAXMASMSMXSAMSSMXAMAMXMMMSAMAMX",
    "XMXSXMMXMXXAAAMMMXMASMXMXSMMAMAMXXMMSXAXMASXMXMAMASMMSAXMAMAMAMAMASXMSASXAAMXMASMSMSXSAMXMMMAXXAMXXXMMXSXMAMMAMMMAXAAXMXAXMAAMSMSMAAAAASXXMM",
    "SXMAMSSMMSMMMSMAMMSAMAASMMAMMMAMMSMSMMAMXXMASAMASXMAASASMSMXXMSMSASXAMAMMMSMAXAMAMXSAAMSMMAMMSSSSSXSMSASMMSSXASAXXMSSMAXMMSMMMMAMASXMXSASMXS",
    "ASAXXAAAXXXAXMXMSASAMXMXAXXXAMXMAAXAMXSXSMSMSASASAMMMMAMAXMMXXAAXAXMXMAMAXMXMSMMXXAMMMMAMXASMXAMAMASAAAXMAXAMAXMAXMAMXSSMAAAAAMAMXAMXMMMMMAX",
    "MXSMMMXSMMSSSXSMMXSSMMXSSMSSMSSMSSSXSAXAMAAASAMMSMSSSMMMXMASMMXSAMMMAMASXXAAXAXXAMSSMXSAXSASXMAMXMAMMMXMMMXMMSXMSXMASAMAMSSSXSSSSSMSAXMXXMMM",
    "XAAMAXXMAAMAAASXSXXMMMAXMAXAAAAMAMXAMXMAMSMXMAMXMXAAASAMXSXMASAMMMAXSSMSMSSMSXSMMXAAMMSAMMSMMSMMMMSSSMXSXMXXXXXSMASAMMXAMMXXMAMXAAXSASMMMMSS",
    "MMXMMSASMSMMMMMAXAMMAMMMMMMXMMSMAMMXMMSMMMXMXAMXSMMSMMSAMXSSSMXSSSSSMAAXXAAXMXMAMMSSMMMXMXMXAAMAAXXAMMAMMMAMXAXASXMXASXSXSASMSSMXMASXXAXXAAX",
    "MSSMXSMMAAMMMSMXMMMSAMAASASASMXMSXMASAAMXMAMMMXXXMAMXMAMSAXMAMAXAAMMMMMMMSSMXAXAMMAAAXSXMASMSMSSSMMSMMAXAASMMMSMMXSMXSAXXMASAAAMSAMXXSMMMMSS",
    "XAAAAXXMXMMAAMXSMMASASMXSASASAXXMASASMMMXSSSXSASMSASMMMMMAMSAMXMMSMSAMXAMMAMSMSMSMSSMMSAMASAMAAAAAAAAXXSSMMAAAAAMSXMAMXMXMAMMMSMMXMAXMXSXAAX",
    "MSSMXXAXXXSMMSAMASASAMXAMAMMMMMXSAMASMMSAAAAAAAMAMXAAASAXXMXAMXMAMAMXSXSMSMXAAAAAAXAXASAMASXMMMSMSSSSMMXMASMMSSSMSMMASASAMMAMXAAXAASXMAMMMSS",
    "XXXAMMMMSMMSSMXMAMXXMMMXMAMAAAMAMXMXMAAMMMMMMMAMXMXMSMSASXSXSMAMXSAMASAMAAAXMMMSMXXAMXXAMAMAMSMMXAXAAAMASXMMAMAMASASASXSASMMSSXSMMXMSMASAMAM",
    "SAMXMASXMAAXXAAMSMSXMXXMSSSSXSMXXSMSMMMSMMAMSAMAMXMXMASAMAMAMMASXXAMASAMSMMMSAMMXMMSMXSSMSSSMSAMMMMXMMMAMMSMAMSMMMXMXSAMAMAAMAMMMSAMXSASXMAS",
    "AXSMSXSASMMMMMMXMAXAMSMXAXAMAMXSXSASMMMAXMAXAAXMAAAXMASAMXMAMSASASMMMMAMXMXAXAMAAMXXAMXXAXAXAMSMAAMSSSMMMAAMAMAAXMMXAXXXAXMMMSAAAXMAMXXMMSMS",
    "MSXAXASAMMSAMASASAMXMAAMXSAMXMAMAMAMMXMASXSMSSMXSXSMMMSAMXMMMMAXAAXXXSAMSSMASXMSMSMSMMXMXMMMXMASMMSAAAASMSSSSSSMMAMMXXSMSMAAAXSMMSMXSMSMXAAX",
    "XAMSMMMXMASASASASAMXAXMMMMXXXMAMSMSMSXMASAXAMMMXMAXAAAXAMSMSSMSMSMXSAAXXAASAMAXAAAAMMMAMAMXAAMMAMSMMSMMMAAAXAAAMSAMASXSAASMMSMMMMAMMSAMXSMSM",
    "AXAAMAMMMMSAMAMXMAMMSMXAAMAMMSAMXAAXSAMAMXMASAMSMMSSMSSMMXXAAXXAAAAMXMMMXXMXSAMMMMXMASMSSMSSXSXSXSAAMXSMMMSSMMMMSAXXXAMMMSXAAAAXXMASMXMMMMXA",
    "MXXXSASAMXMXMXMXSXMXAASMMXAAAAAMMMMMSAMXMAMXSAMXAAXXXMAMAAMSSMMMMMMMAAXMSMMAMAXXMSASXSXAAMAAXSAMASMMSASASXXXAMXXSXMSMXMSXSMSSSMSXXMXXSXSXASM",
    "MAXXAMXXXMASXSAMXASMMXMAASMSMXSMAAXMSAMASMMASXMSMMSMXXAMMMAXXAMAMXSXSMSAAAMXSXMSAMXSASMSSMMSMMAMAMMXMMSAMXAXSMMXMASXAXXAASAAAAAAXSXMMAASMMMA",
    "MAMAAMSXSAMXAAMASAMASXSMMAMAMMAMSMSASMSMASAXSAMXAAXXAMMXMASXMSMSMXMAMXMXMSMAMAAXMMAMXMAAXMAMASXMASAAXAMAMMSAAMAASMAXMMSMMMMMXMMMXSASMMXMASAX",
    "MSSMSXMASAMMXMAAMAMAXXXXSMSAMSAMXXMMXAXMASMXSMMSMMSMXSAAXAMAAAXMXMSMSASMSMMASMMMXMAXAMMMXMSSMMMAAXMSXMSMMAMMMMSXSXMMAAXAXSXSXMASASXMSAMXSMSS",
    "MAAXAAMAMAMAAXMXSMMMXMSXSXMAXMAMMAMXMMMMAXXAMXAMMXAAAMMSMASMMMXMAAXXMAMXAXSMXXAAAMXSXSAXASMMMASMMSAXAXAASXSAXXXXMAXXMSMXMSASASXMASXMMXAMXAXX",
    "MSSMSXMASAMXXXMXSXAXSMSAMXSSMSMMSAMAMSAMMSMMSMXSMSMSMMAXXXMASXAXASXXMAMMSXMXXSMSSMMAXMXMXMAASXMAXXAMAMMMSASMSMMAMSMSMMMXAXAXAMAMAMXSAMSXMSMM",
    "MXMAMXXMSMSXSAAAMMXMAAMXMAMAMXMAMASAMSAMMAMXAMMAXMXAAMASASAMXSMMAXAXSAMMMASAMAMAAASMSSMSASXMSMMSMMSMMMMAMXMAMXMAMMASAAAMSMXMASXMXXAMAMXAMAAX",
    "SAMAMAMXMAAASMMAMSSSMXXSMXSAMAMASMMXXSMMXSSSXSSMASMSSMSXAXXMAAMMSMSMSASXSAMASAMXSMAASASAMXAAXXAASAMAMXMASXMAMMSXSMAMMMMMAAXSAMXXXMMSSMSXMSSM",
    "XAMASAAAMMMXMXSXSAAXXSXAAASAXXSAXXMSAMXAXMAMSXAXMAAAXXXMMMSMMMXAXAMAMAMXMXSMMMXXAXMSMSAMXMMMMMSSMSSXMMSASAMSSMAAXMAMMXSMMMMMAMMSMAAAMMXAAAAA",
    "SMMASXSMSXMASAMXMMSMSMMMMMXAMMMMXSXXXMMMSMAMMSAMXMMSMXAMXAMXMAMSMMMAMAMXSMSXAAXSAMXXMXXXAAXAXAMAAAXASAMXSAMAAAMMMMAMMAMMSMMSMMAAXMMSSMMMMSSM",
    "MSAMXMAXMAMASMSXXMMXAAAXAMMSMMASAXMMXMAXXMAMXAXAAXXAAXSMMMMAMAXXASXXMSXMXAMMMMXXMMSMMAMSMSMSMSSMMMMMMSXMMAMMMMMSXXSXMAMAAAXAMSSSXSAMAXXAXAMX",
    "XAXMSXMAXSMASAMMSMMXSXMSMSAXASAMMAAMXMAXMSMXMMXSMMSMSMMAASMXSXMSAMAAXXAMMSMAXMXMAAXAMAXAAXAXAAXAAXXSAMXSXMXXSAMXAMXASASXSSMAMAAAAMASAMMMMASX",
    "MMAMXAXAAMMMMMMASAAMMAMXMMXSAMXMXAMXAAMSAAMASXMMSMAXXXSSMSAMSAMMAMXMMXAMXMSSSMASMMSSMMXMSMXMMMSXMMAMASAMXMAASAMXSXSAMASAAAXSMMMMXSMMMSAAMMMX",
    "AXSMAMMMXMAMAXMASXMASAMAMXMMAMASXSSMSSMAMXSXSAMAAXSMSXXMMMAMMAMSMMMAAXSAMMXMAMXSAMAAAASXXXXSXMSXMXSMMMAMAMXXSSMAMAAXMXMMSAMXAXSXXXAAASMSMAAX",
    "SXXAASAXASAMXAMXXAMXSASASMSSXMXSAAXAMAXXSMSMSAMSMSAAXMMAASXMSAMXAAXMMMMAMXASMMMSAMSSMMSAAMXMAXMASAXAMSASASMAMAMASMSMSXSMXMASXMXXXSSMXSAMXMSS",
    "MAMSMSASMSASXAMAMAMAXXMXSMASMMMMMMMMMMXXAAXASXMAXSMSMAMSMSAMXMMSXMXSMSMSMSMSAXASAMXMXXXMXMASAMXMMMSAMSMSMSAXMXMMSAAAXAXMMAMAMXMMXMAXAMAMSMAA",
    "MAMXAXAAASAXXAMXSSMMSSMASAMXMAAMASAXAXXXMMMXMASXXXAMXSMMMSAMXAAXAMASXSAXAAXSAMXSXXXXMSMSMSASASXXAMMAMXXXMMXSMAMXXMMMMAMSAMXMAMAAXXSSMMSMAMXM",
    "SAMMAMMMMMAMSMXMAAAAXXMASAXSSSXSASMSMSMMXASASAMXMMXMAXAAASAMMMMSSMASAMSMXMAMAXMSAMMXAAAAAMAMAAMMSMSMMMSMASAMMAMASAMXSAMXSXMXMASMMMAAAAMSMSSM",
    "SAMMMAMXXMXMXXAASXMMSXMASMMAAMXMASMSXAAAXASASAXXMMSMMSSMMSASAAMAAMAMXMXMXXSSSMASXMMASMXMMMAMXMXAMXAAAAAXXMASASXMSASMMAMAMMMXXXMAAMSSMMXAMAMS",
    "SXMSAMXSXSMXMMXMMXAXXXSXXXXMXMAMXSAMSSSMMAMMMMMXAASAMAMXASASXSMMXMAMAXAMXMXAAMMMAXMAMXMSASASXXMMMSSSMSSSXSMMMMAXSAMASMMASASAMXSASAAAAXXAMASX",
    "XXXMASMMASAASMSSSSMSMXMAMXMMMSMSAMAMMMMXAAXAAASXMAMXMXXMMMMMMXMSSSMSSSMSMSMSMMMSSMMMSAMSASASMSXAAMMMMAAAXAXAXSAMXXSMMAMSXMMXMASXMMSSMMSAMXSM",
    "SMXSAMAMAMSMAAXAAXAAAAMAMAMXAAAMXSXMSASMSXSSMMXAMASXMMSAAASAMSAMXAAAAXAAAAAAXXMAAASAMXMSXMAMAMMMXXAAMMXMXMMMMSASMMSXXAMXXSXSMAMMMAXMAXAAAXXA",
    "AXAMAXXMAMAMMMMMMMSMSXXASXSMSSSMMXAXSASXMXAMMMSXMASAAASMMMSAXAMXSSMMSMSMSMSXSXMAXXMAXMASMMAMAMXMASXMSSSXMXASXSAAAAMMMSSMASAMXAMAMMMMSSSMMSSS",
    "SMMMXXAMXMMSMXAAXAXMAXSXMASAAXAMASXMMAMASMMSAMAAMXSMMMSAMMXMMSAMAAXXXMAXMAMXAXMASXSMMSASASMSXMAMMMAAAAAAXSASAMAMMXSAMAAMAMAMSMSXSMAXAXAAAXMM",
    "XAXAXXSMMMAAAXSMSXMMAMXAMXMMMSMMXMAMMAMXMAASASMXMAXXAXMASMXSAMAMSXMXXXMSMMSAMMSAMXAXXXMSAMXXASASXSMMMSSMMSAMXMMXSASAMSMMAXAMAAAASMMMMSXMSSSX",
    "SMMMSAMASMMMSXXAMXXMAMSSMMMAMMMMXSAMMSMMMMMSXMXAMXSMSXSAMMAMASXMAASAMSXSAAXAXMAMSXSMMMMMMMMSXMAAXAXXXXAMXMXMXAXAMMSSMAXSMSSXMMMSMAMMXSAMXAMS",
    "SAAXMAMAMXAXMAMAMSXSMXMAASMMXAXMAXXSXMASXMAXMXSSSXSAMMMAXMASAMXSSXMASAAMMMSMMMMXSAAXMAMAXAAXXMXMSMMMXMAMXSAMMMMXSAMXSXXXMAMMASMMMAMSASAMMAMA",
    "SMMSSXMASXXSMMMAMXAMXAMSMMASMMMMXSXMASAMAMMSXMAAXAMXMMSSMSASAMAMXMXMMMMMXMAMAAXAMSMMSSSSSMMSASMMAMAAASMMASXSAMSAMASASMSMMASXAXASXMSMASAMSMMM",
    "MASAMAXXXXMSAMSXSMAMSXMMAXAMAMSMXAAMMMASMMMMMAMMMSMSXAAMAMASAMMMAMASAMASXSASMSMXXAMAAAAMXXSAMXMSASMSXSAMASASXSMASAMAXAAAMASMSXXMAMAXXMXMASAX",
    "SXMASMMSMMASAMXAXXAMSMMMSMASAMAAXMAMXMXMXMAMXMXXXMASMMSMMSASXMXMAMAXAXASAMMMAAMXSASXMMMMMMSMAAXMAXAXASXMXSAMMXMAMMMSMMMXMASAMSSSSMMMAAXSXSXS",
    "XXSAMMAAAMASMMMMMSSXSAMAAMXMMSSSMMAMXSMSASXXSXMASMMMXXXAAMXXASMSSSMSSMMSXMAMMMSXSMMAXAXASAMXSXSMAMSMMMSMMMAMXSMMXSAXAMXSAMXXMAXAAMXAMSMSAMMM",
    "MMMMSMSSXMASMAAAMXMASXMSXMAXXAXAAXXSAAAMASMASXMAXAXMASMMXSXSAMXAAAAAMAXMASXSAAXMMMSSMMSMMSSXXMAMXXMAMAAXASXMXAAAAMMXAMXXASXXMXMMMMAMAXMMAMMX",
    "AAASAMXAAMXXXXSXSAMXMAXASMSXMMSSMMXMXSSMAMMAMAMASMMMXXXAAMAMAXMMSMMMXSMSXMASMSMASAMAMAXAAXMASMMMSMSAMSMSMMMMSSMMSSSSMMSSSMMXSMSXASMMSMMXSXXS",
    "SSSSXSMMXSMMMMMAMXXAMSMASMMAAAXXSXXMAXXMASMASXMAXAAXSMSSSSXSMMMAAMXSAMMXMMXSAAASMXSAMMSMSSMAMAAXMASXMMXSAMAAAAMAMAMAAAAMXAXAXAASAMXAMAXAMMMM",
    "XMAXASMMAXAMXAXXXMSMSAMXMAMSMMSAMMSMXSAMXMMAMXMXSMMSXAAXXMAXMAMASXAMMASMXSAMXMSMAXXXMXAAXAMXMSMMSMMMAMAXXXMSSSMASMSSMMSASXMMXSMXXXMMSSMMSAAS",
    "XMAMMMAMXSSMXMXAXMAMAMSSMAMXMXMXMAXXAMAMSSMMSAMASMMMMMMSSMMMSMSAMMXXSASAAMXSXXAMXMMSSSMSSMMSAMXXXAAXXMAMMSXMAXMXSMAAXAXMXXAAAMXMXSXXMXMAMXMX",
    "XMAXXXMMMMXAMMASMMASMXXASXSMMAMAMMSMMSAMMAAXSXSASAAMXAXAXAAXXAMASXSMMASMMMMXMSXMASXAAXXMAMAXMAMXSXMSSMXSAAMMMMMXMXSMMXSMSSMMMMAXAMMMMAMASMSM",
    "SSSSXSAAAMMMMMAXASAMXXSAMSAASASASMSXMAMXMSMMMXSMSMMMSSMMSMMXMMMMMMSXMAMAAXMMAAASASMSMSMSAMASMXMASXMAAXAMXSMASAMASAMASAAAAXAAMXAMXMAAXSSXSAAS",
    "MAAAAMSAMXAAAXASMMMSMMMMSMMMSAMASXXAMMSSMMAASAMXSXMXXAAASASAAXAXMAMAMXSMMSAASMMMMSAAXAASXMASMSMAMAMSSMXSAMXAXAXASASAMSMMMSSMSAMSSSSXMMAMXMAS",
    "MMMMMMMMMSXSXSMXASAAMAAXAAAMMXMXMAMMMAAAASXMMASAXAXMSMMMSASASXSSMASAMMMMAAMMAXXAXMXMXMXMXSAMXAMASAMAMXMAMSMSMSMXMAMXMMXAAMAAAMXAAAAXSMXSMMXX",
    "XAAXAMXMASXMASXSSMSSSXXSSSMSAXMMSAMSAMXSMMMXSMMMSMMAAXAAMAMXMXMAXASXSAAMSSSSSMMSSSMSMSAAXMASMMMAMXMASAXAMXAXAXXASXMMAXMXSMMMMXMMSMMMSAASXMMM",
    "SMSXMXAMMSAMMMAXMAMXMAAMAMXMASMAMMXSASAXAAXAMAAMAMMSXSMXSMMXMXXAMMSMMMMXAAMAASAXAMAAASMSMSSMAAMSSMSASMSSSMAMAMSASAMSXXMAMXSAMXXMAXAAMMMSAASX",
    "MAMAMSXSASAMXMSMSXMAMMMMAAAMASMAXMXSAMXSSMMSSSMMAXXMMSMMSAASAMMAXXSAMSMMMXMSMMMSAMSMMMXAAMAXMXMXAMMXMMXAAMAMAMXXSAMAAASXMAXASXMSASMSMMXXMMAA",
    "MAMAMAAMMSMMMAMXXAMSMSASXMSMASXAXSAMAMMMXAAXMAASMXMAAXAAMXMAAMXMSMMSMAASXSXXXMXMAMAMXSMMSSMSMMMSSMMMSSMSMMMSAMXAXAXMSMMAMSSXMAAMASXMAASMMMMM",
    "MMSAMMXMXXAAAXSAMMMXASASAAXMASMXXMAMAMXAMMMSMAAAXAXMMSMSSMXSSMAXAAAAMXMMAAAMXAMXXMMMASAMAAXXAAXAMXSAAAAMXMASASAMSMMMMASMMMXMMMMMXMASMMMAMXXX",
    "SMSXSMMSSMSASMMAMXAMXMAMMMXXXXAXSMMSMSMMMSAMXXMAXSMSAXAMXAXMAMXSMMSSXXXMXMMMSSMMSSXMASAMSMMSSMMMSASMMMMMSSXSXMXXAMSXXAMXAXAXXAAXAMASAMSSMMSS",
    "SASMAXAXMAXAMXMAMXMXSAMXSXXXSMSSMSAAXAAXAMXSMSMSXXAMXMAMMSMSASMSXAXAMSMMSASXMAASASAMXSXMAXAMAXMXMASXXXXAAMXMXMASMSMAMSMSMSMSSSSMXMAXAMMASAAA",
    "MAMMMMSSMSMSMAMXSXAAAAMAMMSXMAXAAASXSSSMXSAMXXAMAMXMXMAMAMXMASAMXMSAMXAAMXXAMSMMASXMAMXXMMMSAMSAMXMAAXMMXSXSAMXSXAMMMAAAAAMMMAXMXXXSSMXMMMSM",
    "MAMMXMXAAXAXXXSAXMMSSSMAAASAMXMMMMMXAAMAAMASXMAMAAXSXSSXSAMMMMAXAMXXMSMSSMSSMAMMAMAMASMMXAXMAMSASAMAMSXSXSMSMXAMMXSMSMSMSMSXMASMMSMAMASXMAMA",
    "MAMMASXMMMXMMXMMMSAAXXASMASAMSMXSASMMMMMMSXMMAAMXMMXAMXAXAXAXXSSMSASMXAXAAAMMAMMASXSMSAMSSSSSMSAMAMAXAASAMASXMAMXXXXAXMAMAMXMAMAAASMXAMAAAXX",
    "SSXSASAXMASXSAAXAMMSSXMMSASXMAXAMAMAXXAAMXMMAXSSSMMXSMMMMASXSMMAAMASAMXSMMSSXMMSXMASMMAMAAXAAAMXMXSSSMMMAMAMMSMSMMMSXXSASASXMMSMXMSXMASXMXAM",
    "SAAMAMAMMSXAASMMSSMMMMMAXMXXXSMSXSSSMSMMXAAXSXAMMAMAXAAXAMXAMASMMMSMXMAAXAXMASAMXMASASXMMMMSMMMSMXMAAXSSXMXSAMXAAAXMAXMASAMXMXAASMMMSXMXSXSM",
    "MMMMSSXMXMMXMASAAAAAAAMMSSSMXXAAAMAMXSXSMMMAXMMASAMMSSMSSSSMXAMAXXAAAMXSMSMSAMAMXMXSMMXSXXAMXASAMAMSMMASAXAAXMSSSMSMMMMMMXMASMMMMAAMSAMASMAS",
    "SSXXAAASASAAXMXMXXMMXMSAAAAMMMMMMMAMASAMXSMXMAXASXMXXXAXXAAMMSXMMAMXMAXXAMAMXXAMMAMXAMASXMASMMSASMMAAXMSXMASAXMAMMAASMXAAASXSAASMMMXSAMAXSAM",
    "XAMMMSXMASXMSMMSSSSMSAMAMSMMAAAXXMAMXMAMAXAASXMMMMXSMMMMMMMMAMAMXXXSXXAMAMXMSXMXXAAXMMASAMAMAMSAMXMSMMXSXAMXMAXMXXSXMXSXSMSASMMSAXMASXMMMMMS",
    "XAXXMAMMAMXMXMAXXAXAAMSAMXXSXSXSXSXMAMAMXMMMSAAAMSMSAAAAAAAMASAMASAMXMSSXMAMXASASXSSXMXSXMMXAMMXMXMAAMMXMMMSMSSSMMMAMAMMAAXXMAMSMMMMSAMXMMSX",
    "SMMMSAXMASXSAMSSMMMMMXSASXMSAAASAAASASMSMSSMSMMMMAAXXMXSSSMSAXAMXXASXSAMAXMMSMMASAAXXXAMMMSSMSXMMASMSMXASAAAAXMASAXAMAMAMMMMSAMXXMAXSAAAXMAS",
    "XXAAXAMXXSAMXXXMXAAAAXXMMAAMMMMMAMAMXMAAMAAAXXSSSMSMSMXMXMMMMSMMMXMAMMASAMSMSAMXMMMMXMXSAAXAAXMASAMAAASASMXMMMMAMSSSSMSXSAXXXXXMXMXXMASXSXMM",
    "MMMSSXSXXMXMMMSSSMSSSSSSSMXXXMXXSSMSSMSMMSMMSMXAAAXAAMAMXMAXAAAAMAAAMSMMMXSAMXSSMXAAXMASMXSMMMMXMAMSMMMXXAMSXSMXSAXMAMAASXSMMMSAMXSMSAXAMMXA",
    "ASAMAMXMMAXXAXXAAAXAAMAAXAXSMMSMMAXAAAMXMXMASAMSMMMSMSSSXXAMSSSSXMXAMAAAMXMMMAMAASASMMASXASAMASXMXMXAXSXMSMXAMAMMXSAMAMXSASMAAMSASMAMASMXAMX",
    "SMMMASAMMSMSSSMSMMMMMMAMMXMAAXXAXMMSSMMASAMASXXXMXXXAAXMMXAXAAAMXXXSSSSSSMAXMAXMMMXMXMASMMSAMSAMXASMMMMMAMAMXMAMMSMMSXXAMAMMSSSMSXMXMXXMASMS",
    "MAXSAMMMAAMAAXAMXAXASXMXAXAXSASMMXAAAAMAMASASAMXSSMMMMSMMMXMMMMMMMMMAXAAAXXMSSSSSSXSXMXSXMMMMAASAMXAASXAAMMMXSXSXSAAXAMXMAMMAXMMXXMAMSASMXAX",
    "SAMMSMMMSSMMMMMMMSSMXASMMMSAMMAAMMSSSMMSSXMMSAMAXMAXAAAAAMAMXMXMXAAMMMMXMMSMMAAMXMXMASAMAMSAXSXMAXMMMMAMXSMAASXSASMMSXMSSSSMMSMASXSXXSAMAMMM",
    "MASXMMSAMAAAXSASXMAXSXMAAAMXMMSMMMMMMMAAAMMXSAMSSMSXMMSXMSASAMAMSSXSAMXSXMAAMMMMAMAXXMAMAMSAMXAMASMSSMSMMSMMXSAMAMAMXXXAAXXAAXMASMMMMMMMAAXA",
    "SXMXAAMXSSMMMXASASXMMSSSMMSAXXAAAXMASMMSSXXASAMAAMXXMMXXASAMMMAXXAASAXAAAXMXMAAXASXSMSSMSXMMMSAMASMASAAMAMASXMAMMSXMXSMMMMSMSSMASAMAAAMMAXAX",
    "XAMSMMSAXAMXSMMMMAMXAMMASXXXMMXSMMSMSXXAMMSXXAMXSMMMMAXMMMSMXSSSMMMSMMMSSMMMMSMSAMASXAXAMXSXAMAMXXMASMMMMSAMAMXSXMASXMAMAASXMAMXSMSSSMSXMAXM",
    "XMMAAAXMSXSAXAXMAXXMASMASXMSSSMXMAXAXMMASAMMSMMXMAMSAXSMSAAMXMXMXAASASMAXAAMMAMMXSAMMSMSMAMMMSMXSXMMSAXXXMAMMMAMAXAMAAAMSXSASMMMMAXAAAAMMSAA",
    "SMSSSMSXSAMMSSMSMMSMMMMAXAXAAAMMSXSAMXSAMXMAASXXSAMAAXSAASMSAMSSSMMSAMMAMSMSAMMAAMXMXXAAMAMAXAAASXMAXAMSXMSSMMXSSMSXSMMMMASAMXMAMXMSMMMSAXAS",
    "AMAMAMMXMXMAXAAMMMSAAXMASMMMSMMXMAAXAXMXXXMSSSSMMMMMSMMAMMXSXSAAAXMMMMMXMMSMAXMMXSAMXMSMSSSSSMMMSAMXMSMSAAAAXSAMXAAAXASAMMMXMASXSMAAMXAMMXAM",
    "MMXSAMAASAMSSMMMAAMMMXMXMAAAXXXAMMMMSSMSMSAMAMXMASXXMAASXMASXMMSMMXAXMXMAXAXMXXAAAMXAMAXXAAXXXAXSAMXXMASXMMSMMASMSMSMASMSAMXXMAAXASMSMSSSMMM",
    "XXAXAXSXSMSMAMASMMSASXSMSSMMSMSMXXAXXMAAAMAMAMASXSASXSXMAXAMMSMMAXSXSMSMSMMMSMMMXSXMXSXSMMMMMMMMMAXSMMAMASXMAXXMAXAAMXMASMMMSMMMMXXAAAAAMAAA",
    "SMSSSMMAMXAXAMMSAMMAMAMXAXXMAAAMXSSSMMMMSMXXAMXMAMASAAXMMMXXXAAMAMAXMASAMAXAAMSSMMXMAMXXMAMXXASASXMXSMASAMASXMSMXMMMXXMASXMAAAAXSAMMMXMMSSMS",
    "XAAAXAXXMXMMSMMMAMMSMSXMASMSMSSSMAAAAAXXMMMSSSMSSMAMMMXAAMXSSXSMXSMMMXMAMSMSXSAAXAMMAMXMASXSSMSASAXMAMAMASAMXXMAMMMSMMSAMAMSSSMSMASXMMXXXAXX",
    "MMMSMXMAXXMAXAXSXMAMAMXSAMXAMAAAMMMMSXMMMAAAMMXAMMXMXXXMASAXMAXMXMAMXMMXMXAXXMMSMMSSMSSXAMXAAAMXMASMMMMSAMXMAASMMSAAAASASMMMXMMAXMMAASXMSMMM",
    "AMXXMASMMSMASAMXAMASAMAMASXMMMSXMXAXXAMSAMMSSMMMSMSMSAMSASMAMSXMAXAMXXMXAMMMMSAMAMAAMAMMXSMSMMMMSMSXMXAAMASASAMXASXMMMSAMXAMAXSASXMSMMAAAMAX",
    "XSAMXMAMAAMMMMAMSMASAMMSAMAAXAXXMMMMMMMSAMXMAMMMAMMMMAXMAXXAXMASAMSMXASMXAAAAMASMMSSMASAMXAXAAAAAXSASMMSMAAMMAXMASMMSAMAMSXSAAMASXMASXMMMSSS",
    "ASAMXSAMSSSMAXMMXXMSXMXMASMXMASASXSAASASAMASAMASASAXMMMMXMXXSSMMSSXAMSXMSSMXMXAMAMMAXXSAMXSSXMMSSSSMMXMAMXSXSAMXSXMAMASMMAMMMMMXMXSAMXXXXAAX",
    "MXMAMMXMAAAMMMSAMMAMXXASMMXSXXSAMASMSMASXMXSMSXSASXSXMSSMSAAXASAMXMSMXAMAAAXSMMSSMMAMMSAMXMAXXAAMAXXXXXASMMASMMXMAMXSMMMMXXASMMMSXMXSMMSMSSX",
    "XAMSASMMMMMMAAMAMSMSMSMMAMMMXMMXMXMXMMXMMMMMMMMMXMAMXAASAMXMSAMMMSAAMSMMSSMMSAAAXMMAXXSXMMMAMMMSSSMMMSXMSAMXMAXAMXMMXMAXXXSASAAASASASAAXAAXX",
    "ASXXXMAMAMXMMMMAMAMAAMXSAMAMMMMXSAMXMMMMAAAXAXAMAMXMMMASMMXMMMMAAXAMMXAAMXMASMMMSSSMSAMXMAMXXXMXXMAMASXMMXMXSSMMSMSMMSXSAAMASMMXSAMASMMMMMSX",
    "AMAMMSAMASAAXSXSSSSMSSMSXSAMXAAMMAAAAAASMSSSMSSSSSXXXMXMAMMMMAMMSSSXMMXMSXMXXXSAMXAXMAMASXSSMSSXMMSMASAMXASXMAXXAMAAMAMMAMMXMXMAMAMXMXAASMXM",
    "MMAXASASAMMSMSAAAXXXXXAXASASMMMXSAMXSSMXAXAAXXAAMAMSXMAMAMAXXMSXMXMAMSAXXMSMAMXMXMSMSXMASAAMAAMAMSMMXSAMSMSXXSMSXSSSMAXMSSSMSAMXSXMXMSMSAMAS",
    "XXMMMMXMASAXAMMMMMMMAMMMXMXMAAAAASAMXMMMSMXMAMMMMMAXAMAXSSSSMMMMMXSAMMXMAAAMAMAMAMAASXSXMMMMMMSMMAXSAXMMMXMAAMAMAXMAMXXXAAAASXSMXXXAAAMXASAS",
    "XASMXXXMXAMXXXAAXMSAXAAXMSMSSMMSSMXSAMAXAAASAMAAAXXXSMMSMAAMAAAAMAMMXAAXMSXMASASMSMSMAMMSXSXAMAMAMSMAXSAMAMXMMAMSMSSMSAMXSMMMAMAMSSMSSMSAMAS",
    "SXAASMSMSSXAMSXSAAAXSSMMSAAXAXXXXAXSXSASMSMSASXSXSXAAMXAMMMSMMSASXSASMSSMAMSMSXXAXMAMAMASASMMSASXXXMMMSAMSASXSAMAAAAAXXMXXXXMMMSMAAXAAAMAMXM",
    "SMMAMAAMAMXMAXAXMAMMAAAXXAXMMXMMMSMMAAAMXMXSXMAMASMXMASXSMXAXAXAMXMASAAXMAXAMMMMMMMAMAXXMMMAXMASXSXXXAXMMMAXASXSMSMMSMSMAMXMSMMMMMSMMSMSAMXM",
    "MASAMXMMSSSSSSSMSMXSSSMMSSMSXAAMAXAMXMSMXMASAMXMAMAAXMMAMMSMSXMXSAMXMMMSSSMXMAAAAASXSMXSAXSXMMXMAMMSMSSSMMSMXMAAMAXXXAAMASMMAAXSAMXMXAASMSAS",
    "SAMAXMXAMAAAAAMAAMMMAAXAAAASMMSXASMMMXXXMMAXAMAMSSSXXXMAMXAAXXMAMXMAXXXMAMASMSSSMXXXAAAXMASMSAMMSMASAAAAMAAMAMXMXAXSMSMSASXSSSMAXMXASMXMAXXS",
    "MASASMMMSMSMMMMSMSAMXMMSSMMMASAMXSMASMSASMMSSMSSMAAASXSASMMSMAMASXSSSXSMSMAMAMAMXSXSSMMSXXXAXAMAAMMSSMSMMSXSASASMMMXAMXSMMMMAMASXMMMXXMMSMMM",
    "SXMAAMAMXAXAXXAXXSXSXSXAXAASXMAMAMXASAMAMXAAAXXAMMMMXAMXXMAMMAMXXAAAAASAAMMMMMAXXSAXAAMMMMMSMXMASMXMAMMXAAXXMSMXAAAMAMXMASAMAMSXAAAXSSMAASAM",
    "XXMSMSASMMMSSMMMMXASXMMSSSMSASXMASMMSXMSMMMSSMSXMSMSMSMAMMSMMSMSMMMMMMMAMMSAASMMAMMMSAMXAAXAXMAMMMMSAMMMSSMMMMMSSMSMSMASAMMSMSMSMMSAMXMASASX",
    "SXAAASXSASAAXAASAMXMAXAMXXAXAXMSASAMXAMMAXAMAAMXSAAAAAXASAAASMAAXAXSAMXAMASMMAAMXMAXXASXSSSXSAXSAMXSSMAAAXAASAAAAMXAASAMXSAAXAAAMSXXAXAMXMXM",
    "SASMMMASMMMSSSMSSXMSAMXSMMXMXMAMSSMMSXMSXMMSMMMSSMSMSMSXSXSSMMSMSSSXMASMMXSXSSXMXSXMSAMXMAMXAMSAMXXSXSMSSSSMSMSSMMMSMSXXSMMSSMSMXSAMXMASMXSX"
]

table2 = [
    ".M.S......",
    "..A..MSMS.",
    ".M.S.MAA..",
    "..A.ASMSM.",
    ".M.S.M....",
    "..........",
    "S.S.S.S.S.",
    ".A.A.A.A..",
    "M.M.M.M.M.",
    "........."
]

print(find_xmas(table))
print(find_x_mas(table))