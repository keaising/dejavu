from src.model.profile import ProfileModel


def create_profile(session, profile_model):
    session.add(profile_model)


def get_profile_by_mobile(session, mobile):
    return session.query(ProfileModel).filter_by(mobile=mobile).first()
