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
           }

if inp in A3codes:
    print(f"Name: {A3codes[inp][0]} | 2-letter code: {A3codes[inp][1]} | top-level domain: {A3codes[inp][2]}")
