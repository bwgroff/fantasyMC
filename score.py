def pass_score(pass_stats):
    score = 0
    score += 4 * pass_stats['td']
    score += .04 * pass_stats['yards']
    if pass_stats['yards'] > 300:
        score += 3
    score -= pass_stats['int']
    return score


def run_score(run_stats):
    score = 0
    score += 6 * run_stats['td']
    score += .1 * run_stats['yards']
    if run_stats['yards'] > 100:
        score += 3
    score -= run_stats['fumble']
    return score


def rec_score(rec_stats):
    score = 0
    score += rec_stats['rec']
    score += 6 * rec_stats['td']
    score += .1 * rec_stats['yards']
    if rec_stats['yards'] > 100:
        score += 3
    return score


def spec_score(spec_stats):
    score = 0
    score += 6 * spec_stats['kick_td']
    score += 2 * spec_stats['2pt_conv']
    score += 6 * spec_stats['off_fumb_td']
    return score


def offense(pass_stats, run_stats, rec_stats, spec_stats, other_stats):
    score = 0
    score += pass_score(pass_stats)
    score += run_score(run_stats)
    score += rec_score(rec_stats)
    score += spec_score(spec_stats)
    score += other_score(other_stats)
    return score


def bigplay_score(bigplays):
    score = 0
    score += bigplays['sack']
    score += 2 * bigplays['int']
    score += 2 * bigplays['fumb_rec']
    score += 6 * bigplays['int_td']
    score += 6 * bigplays['fumb_td']
    score += 2 * bigplays['safety']
    return score


def point_score(points):
    if points >= 35: return -4
    if points >= 28: return -1
    if points >= 21: return 0
    if points >= 14: return 1
    if points >= 7:  return 4
    if points >= 1:  return 7
    return 10


def spec_score_d(spec):
    score = 0
    score += 6 * spec['kick_td']
    score += 6 * spec['punt_td']
    score += 6 * spec['block_td']
    score += 2 * spec['block']
    return score


def defense(bigplays, points, spec):
    score = 0
    score += bigplay_score(bigplays)
    score += point_score(points)
    score += spec_score_d(spec)
    return score
