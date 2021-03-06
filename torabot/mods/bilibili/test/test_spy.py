from nose.tools import assert_equal, assert_in
from .... import make
from ....core.mod import mod
from .. import name
from .ut import need_scrapyd


@need_scrapyd
def test_spy_contains_kind():
    app = make()
    with app.test_client():
        d = mod(name).spy('{"method": "bangumi"}', 60)
        assert_equal(d['kind'], 'bangumi')
        title = d['content'][0]['title']
        d = mod(name).spy('{"method": "sp", "title": "%s"}' % title, 60)
        assert_equal(d['kind'], 'sp')
        d = mod(name).spy('{"method": "user", "user_id": "928123"}', 60)
        assert_equal(d['kind'], 'user')


@need_scrapyd
def test_spy_bangumi():
    app = make()
    with app.test_client():
        d = mod(name).spy('{"method": "bangumi"}', 60)
        assert_in('content', d)


@need_scrapyd
def test_spy_sp():
    app = make()
    with app.test_client():
        d = mod(name).spy('{"method": "bangumi"}', 60)
        assert_equal(d['kind'], 'bangumi')
        title = d['content'][0]['title']
        d = mod(name).spy('{"method": "sp", "title": "%s"}' % title, 60)
        assert_in('sp', d)


@need_scrapyd
def test_spy_user():
    app = make()
    with app.test_client():
        d = mod(name).spy('{"method": "user", "user_id": "928123"}', 60)
        assert_in('posts', d)
