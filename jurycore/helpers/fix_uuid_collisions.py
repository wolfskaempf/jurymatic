import uuid

from jurycore.models import Delegate, Committee, Delegation


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
    print("Done")
