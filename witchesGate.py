import os
import random
import argparse
from mastodon import Mastodon


def main():
    _DATA_DIR = './data'

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--instance',
                        required=False, default='https://mastodon.social')
    parser.add_argument('-l', '--login',
                        required=False, default='')
    parser.add_argument('-p', '--password',
                        required=False, default='')
    parser.add_argument('-c', '--client-cred',
                        required=False, default='./clientcred.txt')
    parser.add_argument('-u', '--user-cred',
                        required=False, default='./usercred.txt')
    parser.add_argument('-a', '--action',
                        required=False, choices=['open', 'close', 'rules'])

    args = parser.parse_args()

    if not os.path.isfile(args.client_cred):
        Mastodon.create_app(
            'witchesGate',
            api_base_url=args.instance,
            to_file=args.client_cred
        )

    if not os.path.isfile(args.user_cred):
        mastodon = Mastodon(client_id=args.client_cred,
                            api_base_url=args.instance)
        mastodon.log_in(args.login, args.password,
                        to_file=args.user_cred)

    mastodon = Mastodon(client_id=args.client_cred,
                        access_token=args.user_cred,
                        api_base_url=args.instance)


    def get_random_gif(directory):
        gif = random.choice(os.listdir(_DATA_DIR + directory))
        return _DATA_DIR + directory + '/' + gif


    def post_status(content, media = None):
        if media:
            media = mastodon.media_post(media_file=media)

        return mastodon.status_post(status=content, media_ids=[media],
                                    visibility='public')


    def open_the_gates():
        gif = get_random_gif('/open')
        return post_status('#WitchesTown', media=gif)


    def close_the_gates():
        gif = get_random_gif('/close')
        return post_status('#witchesTown', media=gif)


    def show_the_rules():
        with open(_DATA_DIR + '/rules.txt', 'r') as content_file:
            content = content_file.read()
        return post_status(content)


    switcher = {
        'open': open_the_gates,
        'close': close_the_gates,
        'rules': show_the_rules
    }

    func = switcher.get(args.action, lambda: None)
    func()


if __name__ == '__main__':
    main()
