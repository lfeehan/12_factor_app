from flask import render_template, url_for, redirect, jsonify

from . import site
from ..models import User, db
from ..forms import NameForm


# custom 404 handler
@site.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@site.route('/', methods=['GET'])
def index():
    """
    Get all users and display main control page
    :return:
    """
    users = User.query.all()
    return render_template('site/index.html', users=users)


@site.route('/users/<string:id>', methods=['GET', 'POST'])
def user_config(id):
    """
    Get or update a user details to the mongo store
    :param id: mongo_id
    :return:
    """
    user = User.query.get_or_404(id)
    form = NameForm(obj=user)
    if form.validate_on_submit():
        if user:
            user.name = form.name.data
            user.quantity = form.quantity.data
            user.price_high = form.price_high.data
            if user.category != form.category.data:
                # TODO: Temporarily not allowing this, its complicated
                return jsonify({}), 500
            user.save()
            return jsonify({}), 200
        else:
            return jsonify({}), 404
    return render_template('site/user_crud_edit.html', user=user, form=form)


@site.route('/users/delete/<int:id>', methods=['POST'])
def user_delete(id):
    """
    delete a user from mongo store, not from blockchain
    :param id: mongo_id
    :return:
    """
    User.query.filter_by(id=id).delete()
    return redirect(url_for('site.users'))
