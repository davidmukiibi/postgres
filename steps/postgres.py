from behave import given, when, then, step
from subprocess import Popen, PIPE


@given("I have a docker container running")
def step_impl(context):
  context.container_name = "postgresql14f42"
  proc = Popen(["docker", "run", "-i", "-d", "--name", context.container_name, "postgres"], stdout=PIPE, stderr=PIPE)
  container_id, err = proc.communicate()
  exitcode = proc.returncode
  assert exitcode == 0
  assert container_id is not False

@when("I run my scripts with ansible they should install postgres into the container")
def step_impl(context):
    proc = Popen(["docker", "exec", context.container_name, "ansible-playbook", "-i", "/tmp/ansible/inventory.ini", "/tmp/ansible/postgres-playbook.yml"], stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    exitcode = proc.returncode

    assert exitcode == 0

@then("Postgres should be running on post 5432")
def step_impl(context):
    proc = Popen(["docker", "exec", context.container_name, "bash", "-c", "exec 7<>/dev/tcp/127.0.0.1/5432"], stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()

    assert proc.returncode == 0

