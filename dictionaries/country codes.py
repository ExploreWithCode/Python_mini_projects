# Alpha-2 codes (2 numbers) and Alpha-3 codes (3)
inp = input("Give me a country's 2-letter or 3-letter code and you will receive more info:\n")
inp = inp.upper()
A2codes = {'AF': ['Afghanistan', 'AFG', '.af'],
           'AX': ['Åland', 'ALA', '.ax'],
           'AL': ['Albania', 'ALB', '.al'],
           'DZ': ['Algeria', 'DZA', '.dz'],
           'AS': ['American Samoa', 'ASM', '.as'],
           'AD': ['Andorra', 'AND', '.ad'],
           'AO': ['Angola', 'AGO', '.ao'],
           'AI': ['Anguilla', 'AIA', '.ai'],
           'AQ': ['Antarctica', 'ATA', '.aq'],
           'AG': ['Antigua and Barbuda', 'ATG', '.ag'],
           'AR': ['Argentina', 'ARG', '.ar'],
           'AM': ['Armenia', 'ARM', '.am'],
           'AW': ['Aruba', 'ABW', '.aw'],
           'AZ': ['Azerbaijan', 'AZE', '.az'],
           'BS': ['Bahamas', 'BHS', '.bs'],
           'BH': ['Bahrain', 'BHR', '.bh'],
           'BD': ['Bangladesh', 'BGD', '.bd'],
           'BB': ['Barbados', 'BRB', '.bb'],
           'BY': ['Belarus', 'BLR', '.by'],
           'BE': ['Belgium', 'BEL', '.be'],
           'BZ': ['Belize', 'BLZ', '.bz'],
           'BJ': ['Benin', 'BEN', '.bj'],
           'BM': ['Bermuda', 'BMU', '.bm'],
           'BT': ['Bhutan', 'BTN', '.bt'],
           'BO': ['Bolivia', 'BOL', '.bo'],
           'BQ': ['Bonaire, Sint Eustatius and Saba', 'BES', '.bq (and .nl)'],
           'BA': ['Bosnia and Herzegovina', 'BIH', '.ba'],
           'BW': ['Botswana', 'BWA', '.bw'],
           'BV': ['Bouvet Island', 'BVT', '.bv(not in use), .no'],
           'BR': ['Brazil', 'BRA', '.br'],
           'IO': ['British Indian Ocean Territory', 'IOT', '.io'],
           'BN': ['Brunei Darussalam', 'BRN', '.bn'],
           'BG': ['Bulgaria', 'BGR', '.bg'],
           'BF': ['Burkina Faso', 'BFA', '.bf'],
           'BI': ['Burundi', 'BDI', '.bi'],
           'CV': ['Cabo Verde', 'CPV', '.cv'],
           'KH': ['Cambodia', 'KHM', '.kh'],
           'CM': ['Cameroon', 'CMR', '.cm'],
           'CA': ['Canada', 'CAN', '.ca'],
           'KY': ['Cayman Islands', 'CYM', '.ky'],
           'CF': ['Central African Republic', 'CAF', '.cf'],
           'TD': ['Chad', 'TCD', '.td'],
           'CL': ['Chile', 'CHL', '.cl'],
           'CN': ['China', 'CHN', '.cn'],
           'CX': ['Christmas Island', 'CX', '.cx'],
           'CC': ['Cocos (Keeling) Islands', 'CC', '.cc'],
           'CO': ['Colombia', 'CO', '.co'],
           'KM': ['Comoros', 'KM', '.km'],
           'CD': ['Congo', 'COD', '.cd'],
           'CK': ['Cook Islands', 'COK', '.ck'],
           'CR': ['Costa Rica', 'CRI', '.cr'],
           'CI': ["Côte d'Ivoire", 'CIV', '.ci'],
           'HR': ["Croatia", 'HRV', '.hr'],
           'CU': ["Cuba", 'CUB', '.cu'],
           'CW': ["Curaçao", 'CUW', '.cw'],
           'CY': ["Cyprus", 'CYP', '.cy'],
           'CZ': ["Czechia", 'CZE', '.cz'],
           'DK': ["Denmark", 'DNK', '.dk'],
           'DJ': ["Djibouti", 'DJI', '.dj'],
           'DM': ["Dominica", 'DMA', '.dm'],
           'DO': ["Dominican Republic", 'DOM', '.do'],
           'EC': ["Ecuador", 'ECU', '.ec'],
           'EG': ["Egypt", 'EGY', '.eg'],
           'SV': ["El Salvador", 'SLV', '.sv'],
           'GQ': ["Equatorial Guinea", 'GNQ', '.gq'],
           'ER': ["Eritrea", 'ERI', '.er'],
           'EE': ["Estonia", 'EST', '.ee'],
           'SZ': ["Eswatini", 'SWZ', '.sz'],
           'ET': ["Ethiopia", 'ETH', '.et'],
           'FK': ["Falkland Islands", 'FLK', '.fk'],
           'FO': ["Faroe Islands", 'FRO', '.fo'],
           'FJ': ["Fiji", 'FJI', '.fj'],
           'FI': ["Finland", 'FIN', '.fi'],
           'FR': ["France", 'FRA', '.fr'],
           'GF': ["French Guiana", 'GUF', '.gf'],
           'PF': ["French Polynesia", 'PYF', '.pf'],
           'TF': ["French Southern Territories", 'ATF', '.tf'],
           'GA': ["Gabon", 'GAB', '.ga'],
           'GM': ["Gambia", 'GMB', '.gm'],
           'GE': ["Georgia", 'GEO', '.ge'],
           'DE': ["Germany", 'DEU', '.de'],
           'GH': ["Ghana", 'GHA', '.gh'],
           'GI': ["Gibraltar", 'GIB', '.gi'],
           'GR': ["Greece", 'GRC and GRE', '.gr'],
           'GL': ["Greenland", 'GRL', '.gl'],
           'GD': ["Grenada", 'GRD', '.gd'],
           'GP': ["Guadeloupe", 'GLP', '.gp'],
           'GU': ["Guam", 'GUM', '.gu'],
           'GT': ["Guatemala", 'GTM', '.gt'],
           'GG': ["Guernsey", 'GGY', '.gg'],
           'GN': ["Guinea", 'GIN', '.gn'],
           'GW': ["Guinea-Bissau", 'GNB', '.gw'],
           'GY': ["Guyana", 'GUY', '.gy'],
           'HT': ["Haiti", 'HTI', '.ht'],
           'HM': ["Heard Island and McDonald Islands", 'HMD', '.hm'],
           'VA': ["Holy See", 'VAT', '.va'],
           'HN': ["Honduras", 'HND', '.hn'],
           'HK': ["Hong Kong", 'HKG', '.hk'],
           'HU': ["Hungary", 'HUN', '.hu'],
           'IS': ["Iceland", 'ISL', '.is'],
           'IN': ["India", 'IND', '.in'],
           'ID': ["Indonesia", 'IDN', '.id'],
           'IR': ["Iran", 'IRN', '.ir'],
           'IQ': ["Iraq", 'IRQ', '.iq'],
           'IE': ["Ireland", 'IRL', '.ie'],
           'IM': ["Isle of Man", 'IMN', '.im'],
           'IL': ["Israel", 'ISR', '.il'],
           'IT': ["Italy", 'ITA', '.it'],
           'JM': ["Jamaica", 'JAM', '.jm'],
           'JP': ["Japan", 'JPN', '.jp'],
           'JE': ["Jersey", 'JEY', '.je'],
           'JO': ["Jordan", 'JOR', '.jo'],
           'KZ': ["Kazakhstan", 'KAZ', '.kz'],
           'KE': ["Kenya", 'KEN', '.ke'],
           'KI': ["Kiribati", 'KIR', '.ki'],
           'KP': ["North Korea", 'PRK', '.kp'],
           'KR': ["South Korea", 'KOR', '.kr'],
           'KW': ['Kuwait', 'KWT', '.kw'],
           'KG': ['Kyrgyzstan', 'KGZ', '.kg'],
           'LA': ['Laos', 'LAO', '.la'],
           'LV': ['Latvia', 'LVA', '.lv'],
           "LB": ["Lebanon", "LBN", ".lb"],
           "LS": ["Lesotho", "LSO", ".ls"],
           "LR": ["Liberia", "LBR", ".lr"],
           "LY": ["Libya", "LBY", ".ly"],
           "LI": ["Liechtenstein", "LIE", ".li"],
           "LT": ["Lithuania", "LTU", ".lt"],
           "LU": ["Luxembourg", "LUX", ".lu"],
           "MO": ["Macao", "MAC", ".mo"],
           "MG": ["Madagascar", "MDG", ".mg"],
           "MW": ["Malawi", "MWI", ".mw"],
           "MY": ["Malaysia", "MYS", ".my"],
           "MV": ["Maldives", "MDV", ".mv"],
           "ML": ["Mali", "MLI", ".ml"],
           "MT": ["Malta", "MLT", ".mt"],
           "MH": ["Marshall Islands", "MHL", ".mh"],
           "MQ": ["Martinique", "MTQ", ".mq"],
           "MR": ["Mauritania", "MRT", ".mr"],
           "MU": ["Mauritius", "MUS", ".mu"],
           "YT": ["Mayotte", "MYT", ".yt"],
           "MX": ["Mexico", "MEX", ".mx"],
           "FM": ["Micronesia", "FSM", ".fm"],
           }

if inp in A2codes:
    print(f"Name: {A2codes[inp][0]} | 3-letter code: {A2codes[inp][1]} | top-level domain: {A2codes[inp][2]}")

A3codes = {'AFG': ['Afghanistan', 'AF', '.af'],
           'ALA': ['Åland', 'AX', '.ax'],
           'ALB': ['Albania', 'AL', '.al'],
           'DZA': ['Algeria', 'DZ', '.dz'],
           'ASM': ['American Samoa', 'AS', '.as'],
           'AND': ['Andorra', 'AD', '.ad'],
           'AGO': ['Angola', 'AO', '.ao'],
           'AIA': ['Anguilla', 'AI', '.ai'],
           'ATA': ['Antarctica', 'AQ', '.aq'],
           'ATG': ['Antigua and Barbuda', 'AG', '.ag'],
           'ARG': ['Argentina', 'AR', '.ar'],
           'ARM': ['Armenia', 'AM', '.am'],
           'ABW': ['Aruba', 'AW', '.aw'],
           'AZE': ['Azerbaijan', 'AZ', '.az'],
           'BHS': ['Bahamas', 'BS', '.bs'],
           'BHR': ['Bahrain', 'BH', '.bh'],
           'BGD': ['Bangladesh', 'BD', '.bd'],
           'BRB': ['Barbados', 'BB', '.bb'],
           'BLR': ['Belarus', 'BY', '.by'],
           'BEL': ['Belgium', 'BE', '.be'],
           'BLZ': ['Belize', 'BZ', '.bz'],
           'BEN': ['Benin', 'BJ', '.bj'],
           'BMU': ['Bermuda', 'BM', '.bm'],
           'BTN': ['Bhutan', 'BT', '.bt'],
           'BOL': ['Bolivia', 'BO', '.bo'],
           'BES': ['Bonaire, Sint Eustatius and Saba', 'BQ', '.bq (and .nl)'],
           'BIH': ['Bosnia and Herzegovina', 'BA', '.ba'],
           'BWA': ['Botswana', 'BW', '.bw'],
           'BVT': ['Bouvet Island', 'BV', '.bv(not in use), .no'],
           'BRA': ['Brazil', 'BR', '.br'],
           'IOT': ['British Indian Ocean Territory', 'IO', '.io'],
           'BRN': ['Brunei Darussalam', 'BN', '.bn'],
           'BGR': ['Bulgaria', 'BG', '.bg'],
           'BFA': ['Burkina Faso', 'BF', '.bf'],
           'BDI': ['Burundi', 'BI', '.bi'],
           'CPV': ['Cabo Verde', 'CV', '.cv'],
           'KHM': ['Cambodia', 'KH', '.kh'],
           'CMR': ['Cameroon', 'CM', '.cm'],
           'CAN': ['Canada', 'CAN', '.ca'],
           'CYM': ['Cayman Islands', 'KY', '.ky'],
           'CAF': ['Central African Republic', 'CF', '.cf'],
           'TCD': ['Chad', 'TD', '.td'],
           'CHL': ['Chile', 'CL', '.cl'],
           'CHN': ['China', 'CN', '.cn'],
           'CXR': ['Christmas Island', 'CX', '.cx'],
           'CCK': ['Cocos (Keeling) Islands', 'CC', '.cc'],
           'COL': ['Colombia', 'CO', '.co'],
           'COM': ['Comoros', 'KM', '.km'],
           'COD': ['Congo', 'CD', '.cd'],
           'COK': ['Cook Islands', 'CK', '.ck'],
           'CRI': ['Costa Rica', 'CR', '.cr'],
           'CIV': ["Côte d'Ivoire", 'CI', '.ci'],
           'HRV': ["Croatia", 'HR', '.hr'],
           'CUB': ["Cuba", 'CU', '.cu'],
           'CUW': ["Curaçao", 'CW', '.cw'],
           'CYP': ["Cyprus", 'CY', '.cy'],
           'CZE': ["Czechia", 'CZ', '.cz'],
           'DNK': ["Denmark", 'DK', '.dk'],
           'DJI': ["Djibouti", 'DJ', '.dj'],
           'DMA': ["Dominica", 'DM', '.dm'],
           'DOM': ["Dominican Republic", 'DO', '.do'],
           'ECU': ["Ecuador", 'EC', '.eu'],
           'EGY': ["Egypt", 'EG', '.eg'],
           'SLV': ["El Salvador", 'SV', '.sv'],
           'GNQ': ["Equatorial Guinea", 'GQ', '.gq'],
           'ERI': ["Eritrea", 'ER', '.er'],
           'EST': ["Estonia", 'EE', '.ee'],
           'SWZ': ["Eswatini", 'SZ', '.sz'],
           'ETH': ["Ethiopia", 'ET', '.et'],
           'FLK': ["Falkland Islands", 'FK', '.fk'],
           'FRO': ["Faroe Islands", 'FO', '.fo'],
           'FJI': ["Fiji", 'FJ', '.fj'],
           'FIN': ["Finland", 'FI', '.fi'],
           'FRA': ["France", 'FR', '.fr'],
           'GUF': ["French Guiana", 'GF', '.gf'],
           'PYF': ["French Polynesia", 'PF', '.pf'],
           'ATF': ["French Southern Territories", 'TF', '.tf'],
           'GAB': ["Gabon", 'GA', '.ga'],
           'GMB': ["Gambia", 'GM', '.gm'],
           'GEO': ["Georgia", 'GE', '.ge'],
           'DEU': ["Germany", 'DE', '.de'],
           'GHA': ["Ghana", 'GH', '.gh'],
           'GIB': ["Gibraltar", 'GI', '.gi'],
           'GRC': ["Greece", 'GR', '.gr'],
           'GRE': ["Greece", 'GR', '.gr'],
           'GRL': ["Greenland", 'GL', '.gl'],
           'GRD': ["Grenada", 'GD', '.gd'],
           'GLP': ["Guadeloupe", 'GP', '.gp'],
           'GUM': ["Guam", 'GU', '.gu'],
           'GTM': ["Guatemala", 'GT', '.gt'],
           'GGY': ["Guernsey", 'GG', '.gg'],
           'GIN': ["Guinea", 'GN', '.gn'],
           'GNB': ["Guinea-Bissau", 'GW', '.gw'],
           'GUY': ["Guyana", 'GY', '.gy'],
           'HTI': ["Haiti", 'HT', '.ht'],
           'HMD': ["Heard Island and McDonald Islands", 'HM', '.hm'],
           'VAT': ["Holy See", 'VA', '.va'],
           'HND': ["Honduras", 'HN', '.hn'],
           'HKG': ["Hong Kong", 'HK', '.hk'],
           'HUN': ["Hungary", 'HU', '.hu'],
           'ISL': ["Iceland", 'IS', '.is'],
           'IND': ["India", 'IN', '.in'],
           'IDN': ["Indonesia", 'ID', '.id'],
           'IRN': ["Iran", 'IR', '.ir'],
           'IRQ': ["Iraq", 'IQ', '.iq'],
           'IRL': ["Ireland", 'IE', '.ie'],
           'IMN': ["Isle of Man", 'IM', '.im'],
           'ISR': ["Israel", 'IL', '.il'],
           'ITA': ["Italy", 'IT', '.it'],
           'JAM': ["Jamaica", 'JM', '.jm'],
           'JPN': ["Japan", 'JP', '.jp'],
           'JEY': ["Jersey", 'JE', '.je'],
           'JOR': ["Jordan", 'JO', '.jo'],
           'KAZ': ["Kazakhstan", 'KZ', '.kz'],
           'KEN': ["Kenya", 'KE', '.ke'],
           'KIR': ["Kiribati", 'KI', '.ki'],
           'PRK': ["North Korea", 'KP', '.kp'],
           'KOR': ["South Korea", 'KR', '.kr'],
           'KWT': ['Kuwait', 'KW', '.kw'],
           'KGZ': ['Kyrgyzstan', 'KG', '.kg'],
           'LAO': ['Laos', 'LA', '.la'],
           'LVA': ['Latvia', 'LV', '.lv'],
           "LBN": ["Lebanon", "LB", ".lb"],
           "LSO": ["Lesotho", "LS", ".ls"],
           "LBR": ["Liberia", "LR", ".lr"],
           "LBY": ["Libya", "LY", ".ly"],
           "LIE": ["Liechtenstein", "LI", ".li"],
           "LTU": ["Lithuania", "LT", ".lt"],
           "LUX": ["Luxembourg", "LU", ".lu"],
           "MAC": ["Macao", "MO", ".mo"],
           "MDG": ["Madagascar", "MG", ".mg"],
           "MWI": ["Malawi", "MW", ".mw"],
           "MYS": ["Malaysia", "MY", ".my"],
           "MDV": ["Maldives", "MV", ".mv"],
           "MLI": ["Mali", "ML", ".ml"],
           "MLT": ["Malta", "MT", ".mt"],
           "MHL": ["Marshall Islands", "MH", ".mh"],
           "MTQ": ["Martinique", "MQ", ".mq"],
           "MRT": ["Mauritania", "MR", ".mr"],
           "MUS": ["Mauritius", "MU", ".mu"],
           "MYT": ["Mayotte", "YT", ".yt"],
           "MEX": ["Mexico", "MX", ".mx"],
           "FSM": ["Micronesia", "FM", ".fm"],
           }

if inp in A3codes:
    print(f"Name: {A3codes[inp][0]} | 2-letter code: {A3codes[inp][1]} | top-level domain: {A3codes[inp][2]}")
