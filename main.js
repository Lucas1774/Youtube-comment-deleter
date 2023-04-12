async function erase() {
  let buttons = [...document.querySelectorAll("c-wiz .GqCJpe.u2cbPc.LDk2Pd .VfPpkd-Bz112c-LgbsSe.yHy1rc.eT1oJ.mN1ivc")];
  for (let button of buttons) {
    button.click();
    await new Promise(res => setTimeout(res, 2000));
  }
}

async function run() {
  while (true) {
    await erase();
    await new Promise(res => setTimeout(res, 2000));
  }
}

run();