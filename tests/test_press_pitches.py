from tests.test_hospital_rankings import FLORIDA_HOSPITALS, _seed

from scripts.build_press_pitches import build_pitches


def test_pitch_uses_the_ranking_numbers(tmp_path):
    _seed(FLORIDA_HOSPITALS)
    [path] = build_pitches(str(tmp_path))
    text = open(path).read()
    assert "Florida hospitals" in text
    assert "6 Florida hospitals" in text
    assert "Bayfront Health St Petersburg" in text and "9.8x" in text
    assert "Sacred Heart Hospital" in text and "2.2x" in text
    assert "/hospitals/fl/most-expensive/" in text


def test_no_pitches_when_no_state_has_enough_hospitals(tmp_path):
    _seed(FLORIDA_HOSPITALS[:3])
    assert build_pitches(str(tmp_path)) == []
