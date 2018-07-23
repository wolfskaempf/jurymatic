import uuid

from jurycore.models import Delegate, Committee, Delegation, Booklet


def fix_collisions():
    delegates = Delegate.objects.all()
    for delegate in delegates:
        delegate.uuid = uuid.uuid4()
        delegate.save()

    committees = Committee.objects.all()
    for committee in committees:
        committee.uuid = uuid.uuid4()
        committee.save()

    delegations = Delegation.objects.all()
    for d in delegations:
        d.uuid = uuid.uuid4()
        d.save()

    booklets = Booklet.objects.all()
    for booklet in booklets:
        booklet.uuid = uuid.uuid4()
        booklet.save()

    print("Done")
