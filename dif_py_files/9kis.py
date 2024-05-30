def main(input_string):
    result = []

    sections = (input_string.strip().
                strip('<:').strip(':>').split('<section>'))

    for section in sections:
        if section:
            parts = section.strip().strip(',').strip().split('<-')
            if len(parts) == 2:
                result.append((parts[0].replace('global `', '')
                               .strip(), parts[1].
                               replace('.</section>', '').
                               replace('. </section>', '')
                               replace('global\n', '').strip()))
    return result
